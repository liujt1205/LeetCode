class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount = 0
        closeCount = 0
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "*":
                openCount += 1
            else:
                openCount -= 1
            if s[len(s) - i - 1] == ")" or s[len(s) - i - 1] == "*":
                closeCount += 1
            else:
                closeCount -= 1
            if openCount < 0 or closeCount < 0:
                return False
        return True