class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = [0] * n
        bottom = [0] * n
        for i in range(1, n):
            bottom[i] = grid[1][i - 1] + bottom[i - 1]
            top[n - i - 1] = grid[0][n - i] + top[n - i]

        best = [0] * n
        for i in range(n):
            best[i] = max(top[i], bottom[i])

        return min(best) 