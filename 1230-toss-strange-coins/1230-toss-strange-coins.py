class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        if target == 0:
            res = 1
            for i in range(n):
                res *= 1 - prob[i]
            return res
        memo = [[0] * (target + 1) for _ in range(n)]
        memo[0][1] = prob[0]
        memo[0][0] = 1 - prob[0]
        for i in range(1, n):
            for j in range(min(i + 2, target + 1)):
                if j - 1 >= 0:
                    memo[i][j] += prob[i] * memo[i - 1][j - 1]
                memo[i][j] += (1 - prob[i]) * memo[i - 1][j]
        return memo[n - 1][target]