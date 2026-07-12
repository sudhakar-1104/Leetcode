class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(index, curr):
            if index == len(nums):
                ans.append(curr[:])
                return

            # Include current element
            curr.append(nums[index])
            backtrack(index + 1, curr)

            # Exclude current element
            curr.pop()
            backtrack(index + 1, curr)

        backtrack(0, [])
        return ans