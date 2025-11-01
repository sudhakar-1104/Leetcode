class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set it to 0 and continue the loop to carry over
            digits[i] = 0
        
        # If all digits were 9, we need an extra 1 at the beginning
        return [1] + digits
