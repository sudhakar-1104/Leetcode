class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        # Binary Search approach
        left = 1
        right = x // 2  # The square root of x will never be greater than x/2 (for x >= 4)
        result = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Use mid * mid to avoid floating point calculations
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                # 'mid' is a potential answer (it satisfies mid^2 <= x)
                # Try the right half for a larger answer
                result = mid
                left = mid + 1
            else: # mid_squared > x
                # 'mid' is too large, search the left half
                right = mid - 1
                
        # 'result' stores the largest integer s such that s*s <= x
        return result