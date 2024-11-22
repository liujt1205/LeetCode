class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        nums = []
        for row in range(m):
            for col in range(n):
                nums.append((grid[row][col], row, col))
                
        nums.sort()
        rows = [0] * m
        cols = [0] * n
        
        for _, row, col in nums:
            val = max(rows[row], cols[col])
            grid[row][col] = val + 1
            rows[row] = val + 1
            cols[col] = val + 1
            
        return grid