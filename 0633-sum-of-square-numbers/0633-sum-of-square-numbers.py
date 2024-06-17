class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        for i in range(int(sqrt(c)) + 1):
            squares.add(i * i)
        for square in squares:
            if c - square in squares:
                return True
        return False