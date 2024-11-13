class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def getPairWithSumSmaller(nums, target):
            left = 0
            right = len(nums) - 1
            res = 0
            while left < right:
                curSum = nums[left] + nums[right]
                if curSum < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
            return res
        
        return getPairWithSumSmaller(nums, upper + 1) - getPairWithSumSmaller(nums, lower)
            