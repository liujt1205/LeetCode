class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * n
        source = [0] * n
        for i in range(len(trust)):
            count[trust[i][1] - 1] += 1
            source[trust[i][0] - 1] += 1
        for i in range(n):
            if count[i] == n - 1 and source[i] == 0:
                return i + 1
        return -1