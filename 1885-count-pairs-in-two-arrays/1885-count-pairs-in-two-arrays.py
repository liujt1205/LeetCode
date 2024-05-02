class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diff = []
        n = len(nums1)
        for i in range(n):
            diff.append(nums1[i] - nums2[i])
        diff.sort()
        left = 0
        right = n - 1
        res = 0
        while left < right and diff[right] > 0:
            while left < right and diff[left] + diff[right] <= 0:
                left += 1
            res += right - left
            right -= 1
        return res
            