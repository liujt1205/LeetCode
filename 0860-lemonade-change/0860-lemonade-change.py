class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0] * 2
        for bill in bills:
            if bill == 20:
                if changes[1] > 0:
                    changes[1] -= 1
                else:
                    changes[0] -= 2
                changes[0] -= 1
            elif bill == 10:
                changes[0] -= 1
                changes[1] += 1
            else:
                changes[0] += 1
            if changes[0] < 0:
                return False
            
        return True