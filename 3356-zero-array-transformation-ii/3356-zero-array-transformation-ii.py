class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        total = 0
        n = len(nums)
        diff = [0] * (n + 1)
        res = 0

        for i in range(n):
            while total + diff[i] < nums[i]:
                res += 1

                if res > len(queries):
                    return -1

                left, right, val = queries[res - 1]
                if right >= i:
                    diff[max(left, i)] += val
                    diff[right + 1] -= val

            total += diff[i]
        
        return res