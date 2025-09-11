class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        
        # Subtract divisor multiples using bit shifts
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            # Double until dividend < temp << 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        
        return -quotient if negative else quotient
