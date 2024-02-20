class Solution:
    def countVowelPermutation(self, n: int) -> int:
        pre = [1] * 5
        mod = 1000000007
        for i in range(1, n):
            cur = [0] * 5
            cur[0] = (pre[4] + pre[1] + pre[2]) % mod
            cur[1] = (pre[0] + pre[2]) % mod
            cur[2] = (pre[1] + pre[3]) % mod
            cur[3] = pre[2] % mod
            cur[4] = (pre[3] + pre[2]) % mod
            pre = cur
        return sum(pre) % mod