class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(base, power):
            if power == 0:
                return 1.0
            half = fast_pow(base, power // 2)
            if power % 2 == 0:
                return half * half
            else:
                return half * half * base
        
        if n < 0:
            return 1 / fast_pow(x, -n)
        else:
            return fast_pow(x, n)
