class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                old_idx = i * n + j
                new_idx = (old_idx + k) % total

                r = new_idx // n
                c = new_idx % n
                ans[r][c] = grid[i][j]

        return ans