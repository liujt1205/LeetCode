class Solution:
    def countOrders(self, n: int) -> int:
        mod = 1000000007
        res = 1
        for i in range(1, n + 1):
            res = (res * i * (2 * i - 1)) % mod
        return res