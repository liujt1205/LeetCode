class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 1000000007
        res = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res = (res + pow(2, right - left, mod)) % mod
                left += 1

        return res