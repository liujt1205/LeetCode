# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        dirs = {"U":(-1, 0), "D":(1, 0), "L":(0, -1), "R":(0, 1)}
        reverse = {"U":"D", "D":"U", "L":"R", "R":"L"}
        isValid = {}
        isValid[(0, 0)] = master.isTarget()
        
        def dfs(row, col):
            for d in dirs:
                drow, dcol = dirs[d]
                new_row, new_col = row + drow, col + dcol
                if (new_row, new_col) not in isValid and master.canMove(d):
                    master.move(d)
                    isValid[(new_row, new_col)] = master.isTarget()
                    dfs(new_row, new_col)
                    master.move(reverse[d])
        
        dfs(0, 0)
        
        queue = deque([(0, 0, 0)])
        seen = set()
        while queue:
            row, col, step = queue.popleft()
            if isValid[(row, col)] == True:
                return step
            
            for new_row, new_col in [[row + 1, col], [row - 1, col], [row, col - 1], [row, col + 1]]:
                if (new_row, new_col) in isValid and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, step+1))
        
        return -1
