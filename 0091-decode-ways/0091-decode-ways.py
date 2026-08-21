class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] = number of ways to decode s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1

        # A single digit is valid only if it is 1-9
        if s[0] != '0':
            dp[1] = 1

        for i in range(2, n + 1):
            # Decode one digit
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Decode two digits
            two_digit = int(s[i - 2:i])

            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]