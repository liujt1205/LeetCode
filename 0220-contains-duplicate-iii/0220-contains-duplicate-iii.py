class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        size = valueDiff + 1
        for i in range(len(nums)):
            bucket = nums[i] // size
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and nums[i] - buckets[bucket - 1] <= valueDiff:
                return True
            if bucket + 1 in buckets and buckets[bucket + 1] - nums[i] <= valueDiff:
                return True
            
            buckets[bucket] = nums[i]
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // size]
                
        return False