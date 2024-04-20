class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col] == 1:
                    height = 0
                    width = 0
                    while height + row < len(land) and land[height+row][col] == 1:
                        height += 1
                    while width + col < len(land[0]) and land[row][col+width] == 1:
                        width += 1
                    res.append([row, col, row+height-1, col+width-1])
                    for i in range(height):
                        for j in range(width):
                            land[row+i][col+j] = 0
        return res