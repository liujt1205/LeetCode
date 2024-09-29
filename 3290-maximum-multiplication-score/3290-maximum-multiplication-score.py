class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        memo = [[-float('inf')] * n for _ in range(4)]
    
        memo[0][0] = a[0] * b[0]
        for i in range(1, n):
            memo[0][i] = max(memo[0][i - 1], a[0] * b[i])

        memo[1][1] = a[0] * b[0] + a[1] * b[1]
        for j in range(2, n):
            memo[1][j] = max(memo[1][j - 1], memo[0][j - 1] + a[1] * b[j])

        memo[2][2] = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
        for k in range(3, n):
            memo[2][k] = max(memo[2][k - 1], memo[1][k - 1] + a[2] * b[k])

        memo[3][3] = a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]
        res = memo[3][3]
        for m in range(4, n):
            memo[3][m] = max(memo[3][m - 1], memo[2][m - 1] + a[3] * b[m])

        res = max(res, memo[3][-1])
        
        return res
