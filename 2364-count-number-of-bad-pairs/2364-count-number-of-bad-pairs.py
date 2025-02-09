class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res = 0
        count = defaultdict(int)
        for i, num in enumerate(nums):
            res += i - count[num - i]
            count[num - i] += 1

        return res