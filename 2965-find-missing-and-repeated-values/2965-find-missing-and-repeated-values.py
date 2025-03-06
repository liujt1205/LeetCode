class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = [0, 0]
        n = len(grid)
        counts = [0] * (n * n)
        for row in range(n):
            for col in range(n):
                cur = grid[row][col]
                counts[cur - 1] += 1

        for i in range(len(counts)):
            if counts[i] == 0:
                res[1] = i + 1
            elif counts[i] == 2:
                res[0] = i + 1

        return res