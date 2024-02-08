class Solution:
    def numSquares(self, n: int) -> int:
        memo = [0] * (n + 1)
        ps = [i * i for i in range(1, int(sqrt(n)) + 1)]
        def check(n):
            if memo[n] != 0:
                return memo[n]
            if n in ps:
                return 1
            else:
                res = float('inf')
                for num in ps:
                    if num > n:
                        break
                    res = min(res, check(n - num) + 1)
                memo[n] = res
                return res
        return check(n)
                    