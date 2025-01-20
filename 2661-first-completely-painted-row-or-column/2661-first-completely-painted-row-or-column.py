class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        index = {}
        for row in range(n):
            for col in range(m):
                index[mat[row][col]] = (row, col)

        rows = [0] * n
        cols = [0] * m
        for i, num in enumerate(arr):
            row, col = index[num]
            rows[row] += 1
            cols[col] += 1
            if rows[row] == m or cols[col] == n:
                return i

        