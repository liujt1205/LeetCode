class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        pre = -float('inf')
        cur = 1
        res = 1
        for num in nums:
            if num - 1 == pre:
                cur += 1
                res = max(res, cur)
            elif num == pre:
                continue
            else:
                cur = 1
            pre = num
        return res