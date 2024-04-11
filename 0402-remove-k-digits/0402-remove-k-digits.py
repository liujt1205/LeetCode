class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        res = []
        for digit in num:
            while k and res and res[-1] > digit:
                res.pop()
                k -= 1
            res.append(digit)
        
        if k > 0:
            res = res[:-k]
        
        return "".join(res).lstrip('0') or "0"