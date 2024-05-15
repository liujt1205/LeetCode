class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        res = 0
        pos = (0, 0, 0)
        
        def valid(row, col, room):
            if 0 <= row < len(room) and 0 <= col < len(room[0]) and room[row][col] != 1:
                return True
            return False
        
        while pos not in visited:
            row, col, d = pos
            visited.add(pos)
            if room[row][col] == 0:
                res += 1
                room[row][col] = 2
            nextRow, nextCol = row + dirs[d][0], col + dirs[d][1]
            if valid(nextRow, nextCol, room):
                pos = (nextRow, nextCol, d)
            else:
                pos = (row, col, (d + 1) % 4)
        return res
                