class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for num in nums:
            if num != 0:
                nums[cur] = num
                cur += 1
                
        while cur < len(nums):
            nums[cur] = 0
            cur += 1
            