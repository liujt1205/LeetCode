class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        curMin = nums[0]
        curMax = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            tempMax = max(num, curMin * num, curMax * num)
            curMin = min(num, curMin * num, curMax * num)
            res = max(res, tempMax)
            curMax = tempMax

        return res