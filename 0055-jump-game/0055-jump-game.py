class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Variable to track the farthest index we can reach
        max_reach = 0
        
        for i in range(len(nums)):
            # If current index is beyond the farthest reachable index → cannot move further
            if i > max_reach:
                return False
            
            # Update the farthest reachable index
            max_reach = max(max_reach, i + nums[i])
            
            # If we can reach or go beyond the last index → success
            if max_reach >= len(nums) - 1:
                return True
        
        return True
