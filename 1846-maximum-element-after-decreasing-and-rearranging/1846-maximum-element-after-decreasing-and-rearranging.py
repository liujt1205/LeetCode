class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        biggest = 0
        for num in arr:
            if num > biggest:
                biggest += 1
        return biggest