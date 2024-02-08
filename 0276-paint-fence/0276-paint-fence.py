class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n > 3 and k == 1:
            return 0
        pre = [0] * 2
        pre[0] = k
        for i in range(1, n):
            cur = [0] * 2
            cur[0] = (pre[0] + pre[1]) * (k - 1)
            cur[1] = pre[0]
            pre = cur
        return sum(pre)