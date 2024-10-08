class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        negative = False
        if n < 0:
            n = abs(n)
            x = 1.0 / x
            
        res = 1
        while n != 0:
            if n % 2 == 1:
                res *= x
                n -= 1
                
            x *= x
            n //= 2
            
        return res