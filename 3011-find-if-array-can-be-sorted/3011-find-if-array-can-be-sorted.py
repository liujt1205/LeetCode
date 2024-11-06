class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        biggest = 0
        prevBiggest = 0
        prevBits = 0
        for num in nums:

            bitCount = num.bit_count()
            if bitCount != prevBits:
                prevBits = bitCount
                prevBiggest = biggest
                biggest = num
            else:
                biggest = max(biggest, num)
            if num < prevBiggest:
                return False
                
        return True
                