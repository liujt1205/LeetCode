class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        for num in sorted(count.keys(), key=lambda x: -x):
            if count[num] == 1:
                return num
            
        return -1