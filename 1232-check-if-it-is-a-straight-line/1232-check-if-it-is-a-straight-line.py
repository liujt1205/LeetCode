class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = float('inf')
        for i in range(1, len(coordinates)):
            dx = coordinates[i][0] - coordinates[i - 1][0]
            dy = coordinates[i][1] - coordinates[i - 1][1]
            if dx == 0 and dy != 0 and slope == float('inf'):
                continue
            elif i == 1 and slope == float('inf'):
                slope = dy / dx
            else:
                if slope == float('inf'):
                    return False
                if dx == 0:
                    return False
                if dy / dx != slope:
                    return False
        return True
                