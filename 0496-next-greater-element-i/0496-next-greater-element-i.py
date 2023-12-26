class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = {}
        mini = None
        maxi = None
        res = []
        pre = nums2[-1]
        maxi = nums2[-1]
        memo[nums2[-1]] = -1
        for i in range(len(nums2) - 2, -1, -1):
            cur = nums2[i]
            if cur >= maxi:
                memo[cur] = -1
                maxi = cur
                pre = cur
            elif cur < pre:
                memo[cur] = pre
                pre = cur
            else:
                mini = pre
                while mini <= cur:
                    mini = memo[mini]
                memo[cur] = mini
                pre = cur
        for num in nums1:
            res.append(memo[num])
        return res