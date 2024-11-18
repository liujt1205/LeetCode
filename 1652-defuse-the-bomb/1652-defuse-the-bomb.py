class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)
        if k == 0:
            return res
        
        start, end, curSum = 1, k, 0
        if k < 0:
            start = len(code) - abs(k)
            end = len(code) - 1
            
        for i in range(start, end + 1):
            curSum += code[i]
            
        for i in range(len(code)):
            res[i] = curSum
            curSum -= code[start % len(code)]
            curSum += code[(end + 1) % len(code)]
            start += 1
            end += 1
            
        return res