class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxCount = 0
        freqGroup = defaultdict(list)
        freq = defaultdict(int)
        for num in nums:
            curFreq = freq[num]
            freq[num] += 1
            freqGroup[curFreq + 1].append(num)
            if curFreq + 1 > maxCount:
                maxCount = curFreq + 1
        return maxCount * len(freqGroup[maxCount])