class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if first[index] == -1:
                first[index] = i
            last[index] = i

        res = 0
        for i in range(26):
            if first[i] != -1:
                distinct = set()
                for index in range(first[i] + 1, last[i]):
                    distinct.add(s[index])
                res += len(distinct)

        return res