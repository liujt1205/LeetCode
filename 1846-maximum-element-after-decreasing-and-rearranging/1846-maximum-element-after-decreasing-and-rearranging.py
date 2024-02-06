class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        counts = [0] * (len(arr) + 1)
        for num in arr:
            counts[min(num, len(arr))] += 1
        res = 0
        for i in range(1, len(arr) + 1):
            res = min(res + counts[i], i)
        return res