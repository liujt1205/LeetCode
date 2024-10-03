class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0

        reminder = {}
        reminder[0] = -1
        res = len(nums)
        cur = 0
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            needed = (cur + p - target) % p
            if needed in reminder:
                res = min(res, i - reminder[needed])
            reminder[cur] = i
                
        return res if res != len(nums) else -1
                
                
        