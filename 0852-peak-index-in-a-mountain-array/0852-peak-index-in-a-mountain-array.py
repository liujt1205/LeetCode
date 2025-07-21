class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if mid - 1 >= 0 and arr[mid - 1] > arr[mid]:
                right = mid
            elif mid + 1 < len(arr) and arr[mid + 1] > arr[mid]:
                left = mid + 1
            else:
                return mid