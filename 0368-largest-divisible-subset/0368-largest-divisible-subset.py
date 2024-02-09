class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = [[i] for i in nums]
        for i in range(len(nums)):
            maxlength = 0
            cur = []
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(memo[j]) > maxlength:
                    maxlength = len(memo[j])
                    cur = memo[j][:]
                    cur.append(nums[i])
                    memo[i] = cur
        res = []
        for i in range(len(nums)):
            if len(memo[i]) > len(res):
                res = memo[i]
        return res