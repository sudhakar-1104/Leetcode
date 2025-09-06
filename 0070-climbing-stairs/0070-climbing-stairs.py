class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        a, b = 1, 2  # f(1), f(2)
        for _ in range(3, n+1):
            a, b = b, a + b  # shift window
        return b
