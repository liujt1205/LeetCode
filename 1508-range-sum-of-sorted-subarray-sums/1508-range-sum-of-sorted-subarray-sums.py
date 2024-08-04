class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new_arr = []
        n = len(nums)
        mod = 1000000007
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = cur + nums[j]
                new_arr.append(cur)
        
        new_arr.sort()
        return sum(new_arr[left - 1: right]) % mod