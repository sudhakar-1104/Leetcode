class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # Frequency of characters available from s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = []
        n = len(s)

        # Try to match target prefix as long as possible
        for i in range(n):
            idx = ord(target[i]) - ord('a')

            # If target[i] is available, use it to keep the prefix equal
            if freq[idx] > 0:
                ans.append(target[i])
                freq[idx] -= 1
            else:
                # Cannot continue matching; backtrack to find a position
                # where we can place the smallest larger character.
                break
        else:
            # Entire target can be formed. Need the next permutation.
            # Backtrack from the end.
            i = n

        # Start backtracking from the first unmatched position
        if len(ans) < n:
            i = len(ans)
        else:
            i = n

        while i >= 0:
            if i < len(ans):
                removed = ans.pop()
                freq[ord(removed) - ord('a')] += 1

            if i == 0 and len(ans) == 0:
                pos = 0
            else:
                pos = i

            if pos < n:
                target_idx = ord(target[pos]) - ord('a')

                # Find the smallest available character > target[pos]
                for c in range(target_idx + 1, 26):
                    if freq[c] > 0:
                        ans.append(chr(c + ord('a')))
                        freq[c] -= 1

                        # Append remaining characters in sorted order
                        for j in range(26):
                            ans.extend(chr(j + ord('a')) * freq[j])

                        return ''.join(ans)

            i -= 1

        return ""