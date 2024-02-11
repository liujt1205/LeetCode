class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        curTotal = 0
        for right in range(len(nums)):
            curTotal += nums[right]
            score = curTotal * (right - left + 1)
            while score >= k and left <= right:
                curTotal -= nums[left]
                left += 1
                score = curTotal * (right - left + 1)
            if left <= right:
                res += right - left + 1
        return res