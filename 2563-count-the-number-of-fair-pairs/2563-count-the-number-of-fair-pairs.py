class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def findSmallestLargerThan(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        biggest = nums[-1]
        low = findSmallestLargerThan(nums, lower - biggest)
        high = findSmallestLargerThan(nums, upper - biggest)
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            while high < i and nums[high] + nums[i] <= upper:
                high += 1
            while low < i and nums[low] + nums[i] < lower:
                low += 1
            if low >= i:
                break
            res += min(i, high) - low
            
        return res