class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(nums)):
            if memo.get(target - nums[i], False):
                return [memo[target - nums[i]] - 1, i]
            memo[nums[i]] = i + 1
        