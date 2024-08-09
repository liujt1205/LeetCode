class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        sequence = "2943816729438167"
        reverse = "7618349276183492"
        for row in range(m - 2):
            for col in range(n - 2):
                if grid[row + 1][col + 1] == 5:
                    indexes = [0, 1, 2, 5, 8, 7, 6, 3]
                    border = []
                    for i in indexes:
                        num = grid[row + i // 3][col + (i % 3)]
                        border.append(str(num))
                    border_str = "".join(border)
                    if sequence.find(border_str) != -1 or reverse.find(border_str) != -1:
                        res += 1
        return res
