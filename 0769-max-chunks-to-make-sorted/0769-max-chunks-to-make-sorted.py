class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        prefix_sum = 0
        sorted_sum = 0
        for i in range(n):
            prefix_sum += arr[i]
            sorted_sum += i
            if prefix_sum == sorted_sum:
                res += 1
                
        return res