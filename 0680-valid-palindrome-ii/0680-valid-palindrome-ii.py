class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, start, end, deleted):
            if start > end:
                return True
            elif s[start] == s[end]:
                start += 1
                end -= 1
                return helper(s, start, end, deleted)
            else:
                if deleted:
                    return False
                else:
                    return helper(s, start + 1, end, True) or helper(s, start, end - 1, True)
                
        return helper(s, 0, len(s) - 1, False)