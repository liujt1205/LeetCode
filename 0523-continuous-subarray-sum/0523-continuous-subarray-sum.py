class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        rem = {}
        rem[0] = -1
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % k
            if prefix in rem:
                if i - rem[prefix] > 1:
                    return True
            else:
                rem[prefix] = i
        return False