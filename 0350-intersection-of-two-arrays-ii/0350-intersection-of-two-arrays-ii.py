class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        count = defaultdict(int)
        for num in nums1:
            count[num] += 1
        res = []
        for num in nums2:
            if count[num] > 0:
                count[num] -= 1
                res.append(num)
            if len(res) == len(nums1):
                break
        return res