from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = [0] * 51

        # Check every subarray of size k
        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            # Each distinct number is present in this subarray
            for x in seen:
                count[x] += 1

        # Find the largest number appearing in exactly one subarray
        ans = -1

        for x in range(51):
            if count[x] == 1:
                ans = x

        return ans