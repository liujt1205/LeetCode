class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        space = set()
        
        def getHashValue(x, y):
            return x * 60001 + y
        
        for x, y in obstacles:
            space.add(getHashValue(x, y))
        
        col = 0
        row = 0
        direct = 0
        res = 0
        for i in range(len(commands)):
            if commands[i] == -2:
                direct = (direct + 3) % 4
            elif commands[i] == -1:
                direct = (direct + 1) % 4
            else:
                step = commands[i]
                while step > 0:
                    newCol = col + directions[direct][1]
                    newRow = row + directions[direct][0]
                    if getHashValue(newRow, newCol) not in space:
                        col = newCol
                        row = newRow
                        step -= 1
                    else:
                        break
                res = max(res, col ** 2 + row ** 2)
        return res