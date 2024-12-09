class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result = [False] * len(nums)
        result[0] = 0
        for i in range(1, len(nums)):
            isSpecial = (nums[i] + nums[i - 1]) % 2 != 0
            if isSpecial:
                result[i] = result[i - 1]
            else:
                result[i] = i
                
        res = []
        for start, end in queries:
            if result[end] <= start:
                res.append(True)
            else:
                res.append(False)
                
        return res