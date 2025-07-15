class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [0] * n
        count = [0] * n
        max_length = 0
        res = 0
        for i in range(n):
            length[i] = 1
            count[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

            max_length = max(max_length, length[i])

        for i in range(n):
            if length[i] == max_length:
                res += count[i]

        return res
