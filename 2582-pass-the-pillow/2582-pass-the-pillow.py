class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % (2 * n - 2)
        if time > n - 1:
            return 2 * n - 1 - time
        else:
            return time + 1