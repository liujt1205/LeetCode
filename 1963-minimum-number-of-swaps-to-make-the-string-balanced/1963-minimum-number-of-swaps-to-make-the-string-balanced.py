class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        left = 0
        swap = False
        for char in s:
            if char == '[':
                left += 1
            else:
                if left > 0:
                    left -= 1
                elif swap:
                    swap = False
                else:
                    res += 1
                    swap = True
                    
        return res