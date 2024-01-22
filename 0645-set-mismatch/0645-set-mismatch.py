class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0] * 2
        for i in range(len(nums)):
            cur = abs(nums[i])
            if nums[cur - 1] < 0:
                res[0] = cur
            else:
                nums[cur - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res[1] = i + 1
        return res