class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def perm(x, y):
            res = 1
            for i in range(y):
                res *= x - i
            return res
        if n == 0:
            return 1
        return sum(9 * perm(9, i) for i in range(n)) + 1