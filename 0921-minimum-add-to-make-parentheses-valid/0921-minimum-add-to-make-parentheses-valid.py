class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        left = 0
        for char in s:
            if char == '(':
                left += 1
            elif left == 0:
                res += 1
            else:
                left -= 1
                
        return res + left