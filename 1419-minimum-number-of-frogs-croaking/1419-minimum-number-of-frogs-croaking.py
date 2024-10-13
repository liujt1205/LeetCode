class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        res = 0
        count = [0] * 4
        frogs = 0
        for char in croakOfFrogs:
            if char == 'c':
                count[0] += 1
                frogs += 1
                res = max(res, frogs)
            elif char == 'r':
                if count[0] == 0:
                    return -1
                else:
                    count[0] -= 1
                    count[1] += 1
            elif char == 'o':
                if count[1] == 0:
                    return -1
                else:
                    count[1] -= 1
                    count[2] += 1
            elif char == 'a':
                if count[2] == 0:
                    return -1
                else:
                    count[2] -= 1
                    count[3] += 1
            elif char == 'k':
                if count[3] == 0:
                    return -1
                else:
                    count[3] -= 1
                    frogs -= 1
            else:
                return -1
            
        return res if sum(count) == 0 else -1
                
                    