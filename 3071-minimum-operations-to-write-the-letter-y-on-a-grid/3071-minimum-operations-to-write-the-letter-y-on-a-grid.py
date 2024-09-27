class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        count_y = [0] * 3
        count_out = [0] * 3
        n = len(grid)
        center = n // 2
        for row in range(n):
            for col in range(n):
                if row <= center and row == col or row < center and row + col == n - 1 or row > center and col == center:
                    count_y[grid[row][col]] += 1
                else:
                    count_out[grid[row][col]] += 1
        
        res = n * n
        for i in range(3):
            for j in range(3):
                if i != j:
                    res = min(res, n * n - count_y[i] - count_out[j])
                    
        return res