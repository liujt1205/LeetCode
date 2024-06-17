class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c)) + 1):
            if sqrt(c - i * i) == int(sqrt(c - i * i)):
                return True
        return False