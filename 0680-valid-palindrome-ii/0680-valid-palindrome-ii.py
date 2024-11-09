class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validate(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return validate(s, l + 1, r) or validate(s, l, r - 1)
            l += 1
            r -= 1
                
        return True