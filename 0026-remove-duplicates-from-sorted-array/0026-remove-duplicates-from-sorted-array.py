class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        prev = -1000
        for i in range(len(nums)):
            if nums[i] > prev:
                nums[index] = nums[i]
                prev = nums[i]
                index += 1
                
        return index