class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = 0
        leftSide, rightSide = 0, 0
        while left < right:
            leftSide += nums[left]
            rightSide += nums[right]
            while leftSide != rightSide and left < right:
                if leftSide < rightSide:
                    left += 1
                    leftSide += nums[left]
                    res += 1
                else:
                    right -= 1
                    rightSide += nums[right]
                    res += 1
            leftSide = 0
            rightSide = 0
            left += 1
            right -= 1
        return res