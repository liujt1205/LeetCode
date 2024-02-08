class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n > 3 and k == 1:
            return 0
        if n == 1:
            return k
        pre = k
        res = k * k
        for i in range(3, n + 1):
            cur = (k - 1) * (res + pre)
            pre = res
            res = cur
        return res