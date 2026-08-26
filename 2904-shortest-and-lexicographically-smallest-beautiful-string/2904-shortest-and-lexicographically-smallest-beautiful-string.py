class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # We have exactly k ones
            if ones == k:
                # Remove unnecessary leading zeros
                while left <= right and s[left] == '0':
                    left += 1

                candidate = s[left:right + 1]

                # Candidate is shorter
                if best == "" or len(candidate) < len(best):
                    best = candidate

                # Same length -> lexicographically smaller
                elif len(candidate) == len(best) and candidate < best:
                    best = candidate

                # Move past the first 1 so the next window
                # can search for another group of k ones
                if s[left] == '1':
                    ones -= 1
                    left += 1

        return best