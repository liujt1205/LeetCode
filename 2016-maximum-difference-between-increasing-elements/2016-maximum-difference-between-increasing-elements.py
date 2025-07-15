class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        smallest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
            elif nums[i] > smallest:
                res = max(res, nums[i] - smallest)

        return res