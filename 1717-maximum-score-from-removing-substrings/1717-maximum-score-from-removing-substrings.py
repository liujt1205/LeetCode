class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if x >= y:
            first = "a"
            second = "b"
            larger = x
            smaller = y
        else:
            first = "b"
            second = "a"
            larger = y
            smaller = x
        
        count = [0] * 2
        for char in s:
            if char == first:
                count[0] += 1
            elif char == second:
                if count[0] > 0:
                    count[0] -= 1
                    res += larger
                else:
                    count[1] += 1
            else:
                res += smaller * min(count[0], count[1])
                count = [0] * 2
        
        res += smaller * min(count[0], count[1])
        return res
                