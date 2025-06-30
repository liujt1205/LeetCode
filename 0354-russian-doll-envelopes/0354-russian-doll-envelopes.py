class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        memo = []
        nums = [i[1] for i in envelopes]
        for i in range(len(nums)):
            index = bisect_left(memo, nums[i])
            if index == len(memo):
                memo.append(nums[i])
            else:
                memo[index] = nums[i]

        return len(memo)