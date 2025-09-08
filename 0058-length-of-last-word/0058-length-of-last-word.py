class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing spaces
        s = s.rstrip()
        # Split into words
        words = s.split(" ")
        # Return length of the last word
        return len(words[-1])
