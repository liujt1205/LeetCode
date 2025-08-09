class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        if n == 0:
            return None
        if m == 0:
            mid = n // 2
            if n % 2 != 0:
                return nums2[mid]
            else:
                return (nums2[mid] + nums2[mid - 1]) / 2

        left, right = 0, m
        while left <= right:
            mid = (left + right) // 2
            mid2 = (m + n + 1) // 2 - mid
            left1 = -float('inf') if mid == 0 else nums1[mid - 1]
            right1 = float('inf') if mid == m else nums1[mid]
            left2 = -float('inf') if mid2 == 0 else nums2[mid2 - 1]
            right2 = float('inf') if mid2 == n else nums2[mid2]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                right = mid - 1
            else:
                left = mid + 1