from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def pick_max(nums: List[int], k: int) -> List[int]:
            stack = []
            drop = len(nums) - k

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:k]

        def merge(a: List[int], b: List[int]) -> List[int]:
            res = []
            i = j = 0

            while i < len(a) or j < len(b):
                if a[i:] > b[j:]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1

            return res

        m, n = len(nums1), len(nums2)
        ans = []

        for i in range(max(0, k - n), min(k, m) + 1):
            part1 = pick_max(nums1, i)
            part2 = pick_max(nums2, k - i)

            candidate = merge(part1, part2)
            ans = max(ans, candidate)

        return ans