class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        gotZero = False
        left = -1
        for right in range(len(nums)):
            if nums[right] != 1 and not gotZero:
                gotZero = True
            elif nums[right] != 1:
                while left < right:
                    left += 1
                    if nums[left] == 0:
                        break
                        
            res = max(res, right - left)

        return res