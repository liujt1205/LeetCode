class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        free = 0
        left = 0
        for i in range(n):
            if locked[i] == "0":
                free += 1
            elif s[i] == '(':
                left += 1
            elif s[i] == ')':
                if left > 0:
                    left -= 1
                elif free > 0:
                    free -= 1
                else:
                    return False

        pairs = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == "0":
                pairs -= 1
                free -= 1
            elif s[i] == '(':
                pairs += 1
                left -= 1
            elif s[i] == ')':
                pairs -= 1
            if pairs > 0:
                return False
            if left == 0 and free == 0:
                break
        
        if left > 0:
            return False

        return True
