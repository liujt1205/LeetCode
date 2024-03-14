class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        curSum = 0
        memo = defaultdict(int)
        for num in nums:
            curSum += num
            if curSum == goal:
                res += 1
            res += memo[curSum - goal]
            memo[curSum] += 1
        return res