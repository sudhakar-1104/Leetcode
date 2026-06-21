class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # If the starting point itself has an obstacle, no paths are possible
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # DP array to store number of ways to reach each column in the current row
        dp = [0] * n
        dp[0] = 1 # Base case: 1 way to be at the start
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # Obstacle blocks all paths
                elif j > 0:
                    dp[j] += dp[j - 1] # Current top path + left path
                    
        return dp[n - 1]