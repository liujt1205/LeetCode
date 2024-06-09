class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0] * k
        prefix[0] = 1
        curSum = 0
        res = 0
        for num in nums:
            curSum = (curSum + num % k + k) % k
            res += prefix[curSum]
            prefix[curSum] += 1
        return res