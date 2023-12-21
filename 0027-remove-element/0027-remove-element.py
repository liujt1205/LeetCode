class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        end = len(nums) - 1
        while k <= end:
            if nums[k] == val:
                nums[k], nums[end] = nums[end], nums[k]
                end -= 1
            else:
                k += 1
        return k