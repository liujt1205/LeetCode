class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = 0
        for i in range(k):
            if i == 0 or nums[i] - nums[i - 1] == 1:
                count += 1
            else:
                count = 1
                
        if count == k:
            res.append(nums[k - 1])
        else:
            res.append(-1)
            
        for i in range(k, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1
            else:
                count = 1
                
            if count >= k:
                res.append(nums[i])
            else:
                res.append(-1)
                
        return res