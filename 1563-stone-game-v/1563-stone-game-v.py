from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        # Precompute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(l: int, r: int) -> int:
            return prefix[r + 1] - prefix[l]

        dp = [[0] * n for _ in range(n)]
        
        # max_left[i][j] = max_{i <= k <= j} (get_sum(i, k) + dp[i][k])
        max_left = [[0] * n for _ in range(n)]
        # max_right[i][j] = max_{i <= k <= j} (get_sum(k, j) + dp[k][j])
        max_right = [[0] * n for _ in range(n)]
        
        # Base cases for single elements
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]
            
        # Outer loop: length of interval
        for length in range(2, n + 1):
            mid = 0
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Maintain 'mid' where sum(i..mid) <= sum(mid+1..j)
                if mid < i:
                    mid = i
                while mid < j and get_sum(i, mid) * 2 <= get_sum(i, j):
                    mid += 1
                mid -= 1  # Largest mid index where sum(i..mid) <= total_sum / 2
                
                res = 0
                
                # Case 1: L < R range -> [i ... mid]
                if mid >= i:
                    res = max(res, max_left[i][mid])
                    
                # Case 2: L > R range -> [mid + 2 ... j]
                if mid + 2 <= j:
                    res = max(res, max_right[mid + 2][j])
                    
                # Case 3: Handle boundary condition when left_sum == right_sum
                if mid >= i and get_sum(i, mid) * 2 == get_sum(i, j):
                    res = max(res, max_right[mid + 1][j])
                    
                dp[i][j] = res
                
                # Update max_left and max_right tables
                total_sum = get_sum(i, j)
                max_left[i][j] = max(max_left[i][j - 1], total_sum + dp[i][j])
                max_right[i][j] = max(max_right[i + 1][j], total_sum + dp[i][j])
                
        return dp[0][n - 1]