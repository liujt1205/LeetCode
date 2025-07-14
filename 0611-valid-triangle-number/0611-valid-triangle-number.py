class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        start = bisect_right(nums, 0)
        for i in range(start, len(nums) - 2):
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                while k < len(nums) and nums[k] < nums[i] + nums[j]:
                    k += 1
                res += k - j - 1

        return res