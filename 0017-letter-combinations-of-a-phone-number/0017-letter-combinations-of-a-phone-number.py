class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, path):
            # If the path is complete (same length as digits), add to result
            if index == len(digits):
                result.append("".join(path))
                return
            
            # Get letters for current digit
            for char in phone_map[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()  # backtrack
        
        backtrack(0, [])
        return result
