class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        heights = [[-1] * n for _ in range(m)]
        queue = deque()
        for row in range(m):
            for col in range(n):
                if isWater[row][col] == 1:
                    heights[row][col] = 0
                    queue.append((row, col))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            row, col = queue.popleft()
            cur_height = heights[row][col]
            for dr, dc in dirs:
                newRow = row + dr
                newCol = col + dc
                if 0 <= newRow < m and 0 <= newCol < n and heights[newRow][newCol] == -1:
                    heights[newRow][newCol] = cur_height + 1
                    queue.append((newRow, newCol))

        return heights