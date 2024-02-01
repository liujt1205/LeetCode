class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        nums.sort()
        start = 0
        while start < len(nums):
            cur = [nums[start], nums[start + 1], nums[start + 2]]
            if nums[start + 2] - nums[start] <= k:
                res.append(cur)
            else:
                return []
            start += 3
        return res