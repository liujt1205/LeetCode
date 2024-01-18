class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre = 2
        pre2 = 1
        while n > 2:
            pre, pre2 = pre2 + pre, pre
            n -= 1
        return pre