class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            a = nums[i]
            count = 0
            min_pow = inf
            for j in range(i, n):
                a = gcd(a, nums[j])
                low = nums[j] & -nums[j]
                if min_pow > low:
                    min_pow = low
                    count = 0
                if min_pow == low:
                    count += 1
                cur = a * (2 if count <= k else 1) * (j - i + 1)
                res = max(res, cur)
        return res