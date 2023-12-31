class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        start = [n] * 26
        end = [-1] * 26
        for i in range(n):
            index = ord(s[i]) - ord('a')
            if start[index] == n:
                start[index] = i
            elif i > end[index]:
                end[index] = i
        res = -1
        for i in range(26):
            if end[i] != -1 and (end[i] - start[i] - 1) > res:
                res = end[i] - start[i] - 1
        return res