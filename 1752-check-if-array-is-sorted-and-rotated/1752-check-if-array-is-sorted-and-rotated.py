class Solution:
    def check(self, nums: List[int]) -> bool:
        findPivot = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if findPivot:
                    return False
                findPivot = True
            if findPivot and nums[i] > nums[0]:
                return False

        return True