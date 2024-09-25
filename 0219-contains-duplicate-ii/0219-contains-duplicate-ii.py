class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        loc = {}
        for i, num in enumerate(nums):
            if num in loc and loc[num] >= i - k:
                return True
            else:
                loc[num] = i
        
        return False