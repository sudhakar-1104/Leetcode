class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Base case: if length <= 2, no need to modify
        if len(nums) <= 2:
            return len(nums)
        
        # Pointer 'i' to place the next valid element
        i = 2  
        
        # Start checking from the 3rd element
        for j in range(2, len(nums)):
            # Only keep the element if it's not equal to nums[i-2]
            # This ensures that each element appears at most twice
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        
        return i
