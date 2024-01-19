class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        pre = matrix[0]
        for i in range(1, n):
            cur = [0] * n
            for j in range(n):
                if not j:
                    cur[j] = min(pre[0], pre[1]) + matrix[i][j]
                elif j == n - 1:
                    cur[j] = min(pre[-1], pre[-2]) + matrix[i][j]
                else:
                    cur[j] = min(pre[j - 1], pre[j], pre[j + 1]) + matrix[i][j]
            pre = cur
        res = float('inf')
        for i in range(n):
            res = min(res, pre[i])
        return res