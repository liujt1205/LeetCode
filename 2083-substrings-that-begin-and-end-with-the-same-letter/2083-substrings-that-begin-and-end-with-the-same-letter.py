class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0] * 26
        res = 0
        for char in s:
            index = ord(char) - ord('a')
            count[index] += 1
            res += count[index]
        return res