class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        res = 0
        start = 0
        end = 0
        while end < len(nums):
            freq[nums[end]] += 1
            while freq[nums[end]] > k:
                freq[nums[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res