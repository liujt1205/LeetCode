class Solution:
    def canChange(self, start: str, target: str) -> bool:
        count = [0] * 2
        n = len(start)
        for i in range(n):
            if start[i] == 'L':
                count[0] += 1
            elif start[i] == 'R':
                count[1] += 1
                if count[0] < 0:
                    return False
                
            if target[i] == 'L':
                count[0] -= 1
                if count[1] > 0:
                    return False
            elif target[i] == 'R':
                count[1] -= 1
                if count[1] < 0:
                    return False
            
            if count[0] > 0:
                return False
            
        return count[0] == 0 and count[1] == 0
                
            