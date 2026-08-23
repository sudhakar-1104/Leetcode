class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = sum(int(c) for c in num[:half] if c != '?')
        right_sum = sum(int(c) for c in num[half:] if c != '?')

        left_q = num[:half].count('?')
        right_q = num[half:].count('?')

        diff = left_sum - right_sum
        q_diff = left_q - right_q

        # Bob wins iff the extra '?' can exactly balance the initial sum difference
        # (Each pair of extra '?' allows Bob to contribute a net sum of 9)
        return 2 * diff + 9 * q_diff != 0