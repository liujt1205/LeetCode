class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        start = -1
        maxIndex = -1
        minIndex = -1
        res = 0
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                start = i    
                maxIndex = -1
                minIndex = -1
                continue
            if nums[i] == maxK:
                maxIndex = i
            if nums[i] == minK:
                minIndex = i
            if maxIndex != -1 and minIndex != -1:
                res += min(maxIndex, minIndex) - start
        return res