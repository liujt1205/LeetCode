class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        odd = 0
        even = 1
        mod = 1000000007
        prefix = 0
        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1
            res %= mod

        return res
            