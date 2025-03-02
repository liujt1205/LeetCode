class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        head1 = 0
        head2 = 0
        res = []
        while head1 < len(nums1) and head2 < len(nums2):
            index1, value1 = nums1[head1]
            index2, value2 = nums2[head2]
            if index1 == index2:
                res.append([index1, value1 + value2])
                head1 += 1
                head2 += 1
            elif index1 < index2:
                res.append([index1, value1])
                head1 += 1
            else:
                res.append([index2, value2])
                head2 += 1

        while head1 < len(nums1):
            index1, value1 = nums1[head1]
            res.append([index1, value1])
            head1 += 1

        while head2 < len(nums2):
            index2, value2 = nums2[head2]
            res.append([index2, value2])
            head2 += 1

        return res