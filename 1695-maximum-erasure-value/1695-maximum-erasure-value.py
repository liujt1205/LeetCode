class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = cur = 0
        count = defaultdict(int)
        left = 0
        for num in nums:
            cur += num
            count[num] += 1
            while count[num] > 1:
                count[nums[left]] -= 1
                cur -= nums[left]
                left += 1
            
            res = max(res, cur)

        return res