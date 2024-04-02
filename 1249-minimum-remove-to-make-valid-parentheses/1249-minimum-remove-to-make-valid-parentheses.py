class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = [0] * len(s)
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            elif s[i] == ")":
                if count > 0:
                    count -= 1
                else:
                    temp[i] = 1
        index = len(s) - 1
        while count > 0 and index >= 0:
            if s[index] == "(":
                count -= 1
                temp[index] = 1
            index -= 1
        res = []
        for i in range(len(temp)):
            if temp[i] == 0:
                res.append(s[i])
        return "".join(res)