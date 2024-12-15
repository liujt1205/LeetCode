class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        left = []
        res = [1] * len(nums)
        for i, num in enumerate(nums):
            while left and num >= nums[left[-1]]:
                left.pop()
            if not left:
                res[i] += i
            else:
                res[i] += i - 1 - left[-1]
                
            left.append(i)
            
        right = []
        for i in range(len(nums) - 1, -1, -1):
            while right and nums[i] >= nums[right[-1]]:
                right.pop()
            if not right:
                res[i] += len(nums) - 1 - i
            else:
                res[i] += right[-1] - 1 - i
            
            right.append(i)
            
        return res