class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        curSum = 0
        prefixSum[0] = 1
        res = 0
        for i in range(len(nums)):
            curSum += nums[i]
            res += prefixSum.get(curSum - k, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return res
                
        
        