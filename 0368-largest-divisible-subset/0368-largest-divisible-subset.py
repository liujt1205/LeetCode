class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = [[i] for i in nums]
        length = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and length[j] >= length[i]:
                    maxlength = length[j]
                    cur = memo[j][:]
                    cur.append(nums[i])
                    memo[i] = cur
                    length[i] = length[j] + 1
        res = []
        maxLength = -1
        for i in range(len(nums)):
            if length[i] > maxLength:
                res = memo[i]
                maxLength = length[i]
        return res