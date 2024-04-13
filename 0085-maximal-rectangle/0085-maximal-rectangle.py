class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        for i in range(rows-1, -1, -1):
            count = 0
            for j in range(cols-1, -1, -1):
                if matrix[i][j] == "1":
                    count += 1
                else:
                    count = 0
                memo[i][j] = count
        
        res = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    width = cols
                    height = 1
                    while row+height-1 < rows and width != 0:
                        width = min(width, memo[row+height-1][col])
                        res = max(res, width * height)
                        height += 1
                        
        return res