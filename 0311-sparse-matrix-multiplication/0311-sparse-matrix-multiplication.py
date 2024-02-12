class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for h in range(k):
                    if mat1[i][h] != 0 and mat2[h][j] != 0:
                        res[i][j] += mat1[i][h] * mat2[h][j]
        return res