class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd

        n = len(coins)

        # Remove redundant denominations:
        # If a coin is a multiple of another coin, its multiples
        # are already covered by the smaller coin.
        coins.sort()
        useful = []

        for c in coins:
            if not any(c % x == 0 for x in useful):
                useful.append(c)

        coins = useful
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        # Count how many positive integers <= x are divisible
        # by at least one coin using Inclusion-Exclusion.
        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                mult = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        mult = lcm(mult, coins[i])
                        bits += 1

                        if mult > x:
                            break

                if mult > x:
                    continue

                if bits % 2:
                    total += x // mult
                else:
                    total -= x // mult

            return total

        # Binary search for the smallest x
        # such that at least k valid amounts exist.
        left = 1
        right = min(coins) * k

        while left < right:
            mid = left + (right - left) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left