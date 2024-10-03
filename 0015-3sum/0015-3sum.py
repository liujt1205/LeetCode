class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        res = []

        def twoSum(nums, i, res):
            seen = set()
            j = i + 1
            while j < len(nums):
                target = -nums[i] - nums[j]
                if target in seen:
                    res.append([nums[i], nums[j], target])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1
    
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(nums, i, res)
                
        return res
            
            
            