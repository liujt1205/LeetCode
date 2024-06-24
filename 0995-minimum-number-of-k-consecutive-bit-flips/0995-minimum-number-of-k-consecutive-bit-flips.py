class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        for i in range(len(nums)):
            if i >= k and nums[i - k] == 2:
                cur -= 1
            if (cur % 2) == nums[i]:
                if i + k > len(nums):
                    return -1
                cur += 1
                res += 1
                nums[i] = 2
        return res