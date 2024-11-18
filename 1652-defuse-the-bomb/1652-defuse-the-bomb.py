class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def replace(code, i, k):
            if k == 0:
                return 0
            step = 1 if k > 0 else -1
            curSum = 0
            for _ in range(abs(k)):
                i = (i + step + len(code)) % len(code)
                curSum += code[i]
                
            return curSum
        
        res = []
        for i, num in enumerate(code):
            res.append(replace(code, i, k))
            
        return res