class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        memo = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            curMax = 0
            for i in range(index - k, index + k + 1):
                if 0 <= i < 26:
                    curMax = max(curMax, memo[i] + 1)
            memo[index] = curMax
        res = 0
        for i in range(26):
            res = max(res, memo[i])
        return res