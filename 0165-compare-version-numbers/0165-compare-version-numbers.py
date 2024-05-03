class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = max(len(v1), len(v2))
        for i in range(n):
            if len(v1) <= i:
                cur1 = 0
            else:
                cur1 = int(v1[i])
            if len(v2) <= i:
                cur2 = 0
            else:
                cur2 = int(v2[i])
            if cur1 < cur2:
                return -1
            elif cur1 > cur2:
                return 1
        return 0
            