class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            return self.longestCommonSubsequence(text2, text1)
        pre = [0] * (len(text2) + 1)
        cur = [0] * (len(text2) + 1)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    cur[j] = 1 + pre[j + 1]
                else:
                    cur[j] = max(cur[j + 1], pre[j])
            pre, cur = cur, pre
        return pre[0]