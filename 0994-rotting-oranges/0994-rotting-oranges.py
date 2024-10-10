class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    count += 1
                    
        if count == 0:
            return 0
        
        res = -1
        while queue and count != 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                if not 0 <= row < m or not 0 <= col < n or grid[row][col] == 0:
                    continue
                if grid[row][col] == 1:
                    count -= 1
                grid[row][col] = 0
                queue.append((row-1, col))
                queue.append((row+1, col))
                queue.append((row, col-1))
                queue.append((row, col+1))
            res += 1
            
        return -1 if count != 0 else res