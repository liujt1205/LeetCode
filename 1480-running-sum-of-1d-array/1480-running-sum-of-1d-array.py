class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                res[i] = num
            else:
                res[i] = num + res[i - 1]

        return res