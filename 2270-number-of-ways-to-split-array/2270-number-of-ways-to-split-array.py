class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        res = 0
        cur_sum = 0
        for i in range(0, len(nums) - 1):
            cur_sum += nums[i]
            if cur_sum >= total - cur_sum:
                res += 1

        return res