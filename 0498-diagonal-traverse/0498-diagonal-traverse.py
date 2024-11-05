class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        direct = [(-1, 1), (1, -1)]
        i = 0
        row, col = 0, 0
        def getNext(row, col, i):
            nextRow = row + direct[i][0]
            nextCol = col + direct[i][1]
            if nextCol == n:
                nextRow = row + 1
                nextCol = col
                i = (i + 1) % 2
            elif nextRow == m:
                nextRow = row
                nextCol = col + 1
                i = (i + 1) % 2
            elif nextCol == -1:
                nextRow = row + 1
                nextCol = col
                i = (i + 1) % 2
            elif nextRow == -1:
                nextRow = row
                nextCol = col + 1
                i = (i + 1) % 2
                
            return nextRow, nextCol, i
        
        res = []
        while len(res) < m * n:
            res.append(mat[row][col])
            row, col, i = getNext(row, col, i)
            
        return res