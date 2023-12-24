class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l1 = None
        l2 = None
        start = 0
        res = 0
        for i in range(len(s)):
            if l1 == None:
                l1 = s[i]
                l1s = i
            if l2 == None and s[i] != l1:
                l2 = s[i]
                l2s = i
            if i and s[i] != s[i - 1]:
                if s[i] == l1:
                    l1s = i
                elif s[i] == l2:
                    l2s = i
                else:
                    res = max(res, i - start)
                    start = max(l1s, l2s)
                    if l1s > l2s:
                        l2 = s[i]
                        l2s = i
                    else:
                        l1 = s[i]
                        l1s = i

            if i == len(s) - 1:
                res = max(res, i - start + 1)
        return res
        
            