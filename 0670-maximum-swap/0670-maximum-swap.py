class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        best = sorted(digits, reverse=True)
        i = 0
        while i < len(digits):
            if digits[i] != best[i]:
                break
            i += 1
        
        if i == len(digits):
            return num
            
        for j in range(len(digits) - 1, -1, -1):
            if digits[j] == best[i]:
                digits[j] = digits[i]
                digits[i] = best[i]
                
        return int(''.join(digits))
        