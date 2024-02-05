class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = {}
        for char in s:
            memo[char] = memo.get(char, 0) + 1
        for i in range(len(s)):
            if memo[s[i]] == 1:
                return i
        return -1