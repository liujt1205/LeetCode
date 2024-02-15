class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        count = [0] * (n + 1)
        one = 0
        for i in range(n):
            count[i + 1] = count[i]
            if data[i] == 1:
                one += 1
            else:
                count[i + 1] += 1
        res = float('inf')
        for i in range(n - one + 1):
            cur = count[i + one] - count[i]
            res = min(res, cur)
        return res