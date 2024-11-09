class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= 2 * k:
            return [-1] * n
        
        res = [-1] * n
        curSum = 0
        for i in range(2 * k + 1):
            curSum += nums[i]
        res[k] = curSum // (2 * k + 1)
            
        for i in range(k + 1, n - k):
            curSum += nums[i + k]
            curSum -= nums[i - k - 1]
            res[i] = curSum // (2 * k + 1)
            
        return res
            