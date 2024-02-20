class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        seenN = False
        zeroIndex = -1
        for num in nums:
            index = abs(num)
            if index == n:
                seenN = True
            elif nums[index] == 0:
                zeroIndex = index
            else:
                nums[index] *= -1
        if seenN == False:
            return n
        for i in range(n):
            if nums[i] > 0:
                return i
            if nums[i] == 0 and zeroIndex == -1:
                return i