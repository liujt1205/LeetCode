class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                if count > 0:
                    count -= 1
            res = max(res, count)
        return res