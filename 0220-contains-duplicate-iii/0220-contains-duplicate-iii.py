from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        set_ = SortedList()
        for i in range(len(nums)):
            # Find the successor of current element
            idx = set_.bisect_left(nums[i])
            if idx != len(set_) and set_[idx] <= nums[i] + valueDiff:
                return True

            # Find the predecessor of current element
            if idx > 0 and nums[i] <= set_[idx - 1] + valueDiff:
                return True

            set_.add(nums[i])
            if len(set_) > indexDiff:
                set_.remove(nums[i - indexDiff])

        return False