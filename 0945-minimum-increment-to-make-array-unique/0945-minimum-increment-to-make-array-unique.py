class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        small, large = min(nums), max(nums)
        count = [0] * (large + 2)
        res = 0
        cur = small
        for num in nums:
            count[num] += 1
        while cur <= large and count[large] > 0:
            if count[cur] > 1:
                res += count[cur] - 1
                count[cur + 1] += count[cur] - 1
            cur += 1
        if count[large + 1] > 1:
            res += count[large + 1] * (count[large + 1] - 1) // 2
        return res