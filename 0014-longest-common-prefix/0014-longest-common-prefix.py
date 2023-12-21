class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs:
            i = 0
            while i < len(s):
                if s[i] != res[i]:
                    break
                i += 1
                if i == len(res):
                    break
            if i == 0:
                return ''
            res = res[:i]
        return res
                