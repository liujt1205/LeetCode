class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]

        for row in range(m):
            for col in range(n):
                res[col][row] = matrix[row][col]

        return res