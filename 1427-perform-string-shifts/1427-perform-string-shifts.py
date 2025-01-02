class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        total = 0
        for direct, amount in shift:
            if direct == 0:
                total += amount
            else:
                total -= amount

        move = total % n

        return s[move:] + s[:move]