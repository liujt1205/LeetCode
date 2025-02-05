class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        mis = []
        for i in range(n):
            if s1[i] != s2[i]:
                mis.append(i)
            if len(mis) > 2:
                return False

        if len(mis) == 0 or (len(mis) == 2 and s1[mis[0]] == s2[mis[1]] and s1[mis[1]] == s2[mis[0]]):
            return True
        else:
            return False