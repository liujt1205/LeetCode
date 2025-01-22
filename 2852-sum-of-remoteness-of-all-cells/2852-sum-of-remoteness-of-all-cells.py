class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        all_sum = 0
        all_count = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] != -1:
                    cur_sum = grid[row][col]
                    grid[row][col] = -1
                    cur_count = 1
                    queue = deque([(row, col)])
                    while queue:
                        cur_r, cur_c = queue.popleft()
                        for dr, dc in dirs:
                            new_r = cur_r + dr
                            new_c = cur_c + dc
                            if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] != -1:
                                cur_sum += grid[new_r][new_c]
                                grid[new_r][new_c] = -1
                                cur_count += 1
                                queue.append((new_r, new_c))
                    res -= cur_count * cur_sum
                    all_sum += cur_sum
                    all_count += cur_count
        
        return res + all_sum * all_count

