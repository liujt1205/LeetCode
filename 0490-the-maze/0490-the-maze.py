class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(maze), len(maze[0])
        def goUntilStop(row, col, i):
            while 0 <= row + dirs[i][0] < m and 0 <= col + dirs[i][1] < n and maze[row + dirs[i][0]][col + dirs[i][1]] == 0:
                row = row + dirs[i][0]
                col = col + dirs[i][1]
                
            return row, col
        
        visited = set()
        queue = deque([(start[0], start[1])])
        while queue:
            row, col = queue.popleft()
            if row == destination[0] and col == destination[1]:
                return True
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for i in range(4):
                newRow, newCol = goUntilStop(row, col, i)
                queue.append((newRow, newCol))
                
        return False