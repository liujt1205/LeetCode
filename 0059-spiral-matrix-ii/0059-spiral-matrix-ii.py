class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        
        row, col, direct = 0, 0, 0
        for i in range(1, n * n + 1):
            res[row][col] = i
            row, col, direct = self.getNext(res, row, col, direct)
            
        return res
    
    def getNext(self, res, row, col, direct):
        directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        newRow = row + directs[direct][0]
        newCol = col + directs[direct][1]
        if not 0 <= newRow < len(res) or not 0 <= newCol < len(res) or res[newRow][newCol] != 0:
            direct = (direct + 1) % 4
            newRow = row + directs[direct][0]
            newCol = col + directs[direct][1]
            
        return newRow, newCol, direct