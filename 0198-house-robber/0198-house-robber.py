class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre = 0
        pre2 = 0
        for i in range(len(nums)):
            cur = max(pre, nums[i] + pre2)
            pre2 = pre
            pre = cur
        return pre