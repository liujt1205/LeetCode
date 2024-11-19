class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freqs = {}
        count = 0
        res = 0
        if len(nums) < k:
            return res
        
        curSum = 0
        for i in range(k):
            curSum += nums[i]
            if nums[i] not in freqs:
                freqs[nums[i]] = 1
                count += 1
            else:
                freqs[nums[i]] += 1
        
        if count == k:
            res = max(res, curSum)
            
        for i in range(k, len(nums)):
            curSum += nums[i]
            if nums[i] not in freqs:
                freqs[nums[i]] = 1
                count += 1
            else:
                freqs[nums[i]] += 1
            curSum -= nums[i - k]
            freqs[nums[i - k]] -= 1
            if freqs[nums[i - k]] == 0:
                count -= 1
                del freqs[nums[i - k]]
            if count == k:
                res = max(res, curSum)
        
        return res