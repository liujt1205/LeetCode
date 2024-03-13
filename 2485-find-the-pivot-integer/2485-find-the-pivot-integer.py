class Solution:
    def pivotInteger(self, n: int) -> int:
        res = int(sqrt((1 + n) * n / 2))
        if res * res == (1 + n) * n / 2:
            return int(res)
        else:
            return -1