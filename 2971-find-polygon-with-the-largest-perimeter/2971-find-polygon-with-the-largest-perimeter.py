class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        preSum = 0
        res = -1
        for num in nums:
            if preSum > num:
                res = max(res, preSum + num)
            preSum += num
        return res