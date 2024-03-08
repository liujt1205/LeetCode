class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxCount = 0
        res = 0
        freq = defaultdict(int)
        for num in nums:
            curFreq = freq[num]
            freq[num] += 1
            if curFreq + 1 > maxCount:
                maxCount = curFreq + 1
                res = maxCount
            elif curFreq + 1 == maxCount:
                res += maxCount
        return res