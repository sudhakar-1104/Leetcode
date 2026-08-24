from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Build prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # If Alice takes all stones, this is the initial option
        ans = prefix[n - 1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans