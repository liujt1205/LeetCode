class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        kmp = needle + '#' + haystack
        dp = [0] * len(kmp)
        for i in range(1, len(dp)):
            pre = dp[i - 1]
            while pre and kmp[i] != kmp[pre]:
                pre = dp[pre - 1]

            dp[i] = pre + (kmp[i] == kmp[pre])
            if dp[i] == len(needle):
                return i - len(needle) * 2

        return -1