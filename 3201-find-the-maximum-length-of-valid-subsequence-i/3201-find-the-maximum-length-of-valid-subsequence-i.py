class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        mix = 0
        pre = nums[0] + 1
        for num in nums:
            if (num + pre) % 2 != 0:
                mix += 1
                pre = num
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

        return max(mix, even, odd)