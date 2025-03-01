class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        cur = 0
        while cur < len(nums) - 1:
            if nums[cur] == 0:
                cur += 1
            elif nums[cur] == nums[cur + 1]:
                res.append(nums[cur] * 2)
                cur += 2
            else:
                res.append(nums[cur])
                cur += 1
        
        if cur <= len(nums) - 1 and nums[cur] != 0:
            res.append(nums[cur])

        while len(res) < len(nums):
            res.append(0)

        return res