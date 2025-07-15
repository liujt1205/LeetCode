class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        outer = False
        res = []
        left = 0
        for char in s:
            if char == '(':
                if not outer:
                    outer = True
                else:
                    res.append(char)
                    left += 1
            else:
                if left > 0:
                    res.append(char)
                    left -= 1
                else:
                    outer = False

        return ''.join(res)