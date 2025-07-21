class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        countX = 0
        countL = 0
        countR = 0
        for i in range(n):
            if start[i] == 'L':
                if countR > 0:
                    return False
                countL += 1
            elif start[i] == 'R':
                if countL < 0:
                    return False
                countR += 1
            else:
                countX += 1

            if result[i] == 'L':
                countL -= 1
            elif result[i] == 'R':
                countR -= 1
            else:
                countX -= 1
            
            if countL * countR < 0 or (countL > 0 and countX < 0) or (countX > 0 and countR < 0):
                return False

        return countL == 0 and countR == 0 and countX == 0

        