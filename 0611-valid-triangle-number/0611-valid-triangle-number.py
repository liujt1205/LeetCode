class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        start = bisect_right(nums, 0)
        for i in range(start, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                largest = nums[i] + nums[j]
                index = bisect_left(nums, largest)
                res += index - j - 1

        return res