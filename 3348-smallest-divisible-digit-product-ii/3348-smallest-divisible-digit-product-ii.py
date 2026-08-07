class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t into 2^a * 3^b * 5^c * 7^d
        a = b = c = d = 0
        temp = t
        while temp % 2 == 0:
            a += 1
            temp //= 2
        while temp % 3 == 0:
            b += 1
            temp //= 3
        while temp % 5 == 0:
            c += 1
            temp //= 5
        while temp % 7 == 0:
            d += 1
            temp //= 7
            
        if temp > 1:
            return "-1"

        # Helper to compare two digit count tuples (c2, c3, c4, c6, c8, c9)
        def is_better(T1, T2):
            if T1 is None:
                return False
            if T2 is None:
                return True
            k1 = sum(T1)
            k2 = sum(T2)
            if k1 != k2:
                return k1 < k2
            # Greater count tuple -> smaller lexicographical sorted digit list
            return T1 > T2

        # Step 2: Precompute optimal digit counts for all (a', b')
        grid = {}
        for c2 in range(3):
            for c3 in range(2):
                for c4 in range(2):
                    for c6 in range(2):
                        for c8 in range(17):
                            for c9 in range(16):
                                p2 = c2 + 2 * c4 + c6 + 3 * c8
                                p3 = c3 + c6 + 2 * c9
                                A = min(46, p2)
                                B = min(29, p3)
                                T = (c2, c3, c4, c6, c8, c9)
                                if (A, B) not in grid or is_better(T, grid[(A, B)]):
                                    grid[(A, B)] = T

        best = {}
        for A in range(46, -1, -1):
            for B in range(29, -1, -1):
                cur = grid.get((A, B), None)
                if A + 1 <= 46 and is_better(best.get((A + 1, B)), cur):
                    cur = best[(A + 1, B)]
                if B + 1 <= 29 and is_better(best.get((A, B + 1)), cur):
                    cur = best[(A, B + 1)]
                best[(A, B)] = cur

        def build_suffix(T, c5, c7, rem_len):
            c2, c3, c4, c6, c8, c9 = T
            k = c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
            ones = rem_len - k
            res = []
            if ones > 0:
                res.append('1' * ones)
            if c2: res.append('2' * c2)
            if c3: res.append('3' * c3)
            if c4: res.append('4' * c4)
            if c5: res.append('5' * c5)
            if c6: res.append('6' * c6)
            if c7: res.append('7' * c7)
            if c8: res.append('8' * c8)
            if c9: res.append('9' * c9)
            return "".join(res)

        N = len(num)
        pos0 = N
        for idx, ch in enumerate(num):
            if ch == '0':
                pos0 = idx
                break

        pref_a = [0] * (pos0 + 1)
        pref_b = [0] * (pos0 + 1)
        pref_c = [0] * (pos0 + 1)
        pref_d = [0] * (pos0 + 1)

        digit_powers = {
            '1': (0, 0, 0, 0),
            '2': (1, 0, 0, 0),
            '3': (0, 1, 0, 0),
            '4': (2, 0, 0, 0),
            '5': (0, 0, 1, 0),
            '6': (1, 1, 0, 0),
            '7': (0, 0, 0, 1),
            '8': (3, 0, 0, 0),
            '9': (0, 2, 0, 0),
        }

        for i in range(pos0):
            da, db, dc, dd = digit_powers[num[i]]
            pref_a[i + 1] = pref_a[i] + da
            pref_b[i + 1] = pref_b[i] + db
            pref_c[i + 1] = pref_c[i] + dc
            pref_d[i + 1] = pref_d[i] + dd

        # Check if num itself is valid
        if pos0 == N:
            if pref_a[N] >= a and pref_b[N] >= b and pref_c[N] >= c and pref_d[N] >= d:
                return num

        # Step 3: Prefix Matching for length N
        for i in range(min(N - 1, pos0), -1, -1):
            d_start = int(num[i]) + 1 if i < pos0 else 1
            for d_next in range(d_start, 10):
                da, db, dc, dd = digit_powers[str(d_next)]
                cur_a = pref_a[i] + da
                cur_b = pref_b[i] + db
                cur_c = pref_c[i] + dc
                cur_d = pref_d[i] + dd

                rem_a = max(0, a - cur_a)
                rem_b = max(0, b - cur_b)
                rem_c = max(0, c - cur_c)
                rem_d = max(0, d - cur_d)

                T = best[(rem_a, rem_b)]
                k_suff = sum(T) + rem_c + rem_d
                rem_len = N - 1 - i

                if k_suff <= rem_len:
                    suffix = build_suffix(T, rem_c, rem_d, rem_len)
                    return num[:i] + str(d_next) + suffix

        # Step 4: Construct length > N
        T = best[(a, b)]
        min_len_t = sum(T) + c + d
        L = max(N + 1, min_len_t)
        return build_suffix(T, c, d, L)