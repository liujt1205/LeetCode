class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        prefix_sum[0] = -1
        curSum = 0
        res = 0
        for i, num in enumerate(nums):
            curSum += num
            if curSum not in prefix_sum:
                prefix_sum[curSum] = i
            if curSum - k in prefix_sum:
                res = max(res, i - prefix_sum[curSum - k])
        
        return res