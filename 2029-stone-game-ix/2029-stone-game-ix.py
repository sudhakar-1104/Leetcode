class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c0 = c1 = c2 = 0
        for x in stones:
            rem = x % 3
            if rem == 0:
                c0 += 1
            elif rem == 1:
                c1 += 1
            else:
                c2 += 1
        
        if c0 % 2 == 0:
            # Even 0s: Alice wins if both 1s and 2s exist
            return c1 >= 1 and c2 >= 1
        else:
            # Odd 0s: Alice wins if |c1 - c2| > 2
            return abs(c1 - c2) > 2