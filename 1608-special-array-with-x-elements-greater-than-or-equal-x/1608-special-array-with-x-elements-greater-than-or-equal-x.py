class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        for num in nums:
            freq[min(n, num)] += 1
        
        res = 0
        for i in range(n, 0, -1):
            res += freq[i]
            if i == res:
                return i
        return -1