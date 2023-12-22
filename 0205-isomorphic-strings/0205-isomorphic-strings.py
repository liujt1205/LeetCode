class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        memo = {}
        exist = set()
        target = set()
        for i in range(len(s)):
            if s[i] not in exist:
                if t[i] in target:
                    return False
                exist.add(s[i])
                target.add(t[i])
                memo[s[i]] = t[i]
            else:
                if memo[s[i]] != t[i]:
                    return False
        return True