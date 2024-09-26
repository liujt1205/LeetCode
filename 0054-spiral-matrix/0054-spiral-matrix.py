class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def getNext(row, col, dire, directions, matrix, m, n):
            nextRow = row + directions[dire][0]
            nextCol = col + directions[dire][1]
            if nextRow < 0 or nextRow >= m or nextCol < 0 or nextCol >= n or matrix[nextRow][nextCol] < -100:
                dire = (dire + 1) % 4
                nextRow = row + directions[dire][0]
                nextCol = col + directions[dire][1] 
            return (nextRow, nextCol, dire)
            
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        res = []
        row, col, dire = 0, 0, 0
        while len(res) < m * n:
            res.append(matrix[row][col])
            matrix[row][col] = -200
            row, col, dire = getNext(row, col, dire, directions, matrix, m, n)
            
        return res