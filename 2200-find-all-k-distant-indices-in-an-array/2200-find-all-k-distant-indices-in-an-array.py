class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        targetIndex = []
        for i in range(len(nums)):
            if nums[i] == key:
                targetIndex.append(i)

        last = 0
        for i in range(len(targetIndex)):
            for j in range(max(last, targetIndex[i] - k), min(targetIndex[i] + k, len(nums) - 1) + 1):
                res.append(j)
            last = min(targetIndex[i] + k, len(nums)) + 1

        return res