class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {}
        count = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if counts.get(count, -1) < 0:
                counts[count] = i
            if count == 0:
                res = max(res, i + 1)
            elif counts.get(count, -1) >= 0:
                res = max(res, i - counts[count])
        return res