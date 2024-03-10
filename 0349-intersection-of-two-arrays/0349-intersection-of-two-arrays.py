class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = defaultdict(int)
        for num in nums1:
            memo[num] = 1
        res = set()
        for num in nums2:
            if memo[num] == 1:
                res.add(num)
        return list(res)