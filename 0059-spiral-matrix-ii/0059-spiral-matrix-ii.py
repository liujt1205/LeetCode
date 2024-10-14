class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col, direct = 0, 0, 0
        for i in range(1, n * n + 1):
            res[row][col] = i
            if not 0 <= row + directs[direct][0] < len(res) or not 0 <= col + directs[direct][1] < len(res) or res[row + directs[direct][0]][col + directs[direct][1]] != 0:
                direct = (direct + 1) % 4
            row += directs[direct][0]
            col += directs[direct][1]
            
        return res
