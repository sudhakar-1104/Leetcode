class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        
        for num in nums:
            xor ^= num
        
        if xor != 0:
            return len(nums)
        
        # Total XOR is 0
        # If there is a non-zero element, remove it
        if any(num != 0 for num in nums):
            return len(nums) - 1
        
        # All elements are zero
        return 0