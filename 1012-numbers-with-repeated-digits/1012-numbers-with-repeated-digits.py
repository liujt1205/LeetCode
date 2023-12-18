class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def perm(n, k):
            res = 1
            for i in range(k):
                res *= n - i
            return res
        digits = list(map(int, str(n + 1)))
        length = len(digits)
        res = sum(9 * perm(9, i) for i in range(length - 1))
        s = set()
        for i, x in enumerate(digits):
            for y in range(1, x) if i == 0 else range(x):
                if y not in s:
                    res += perm(9 - i, length - i - 1)
            if x in s:
                    break
            s.add(x) 
        return n - res