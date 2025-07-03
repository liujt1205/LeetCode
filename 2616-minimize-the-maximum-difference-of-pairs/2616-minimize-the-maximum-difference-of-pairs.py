class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def countPairs(nums, limit):
            i = 0
            count = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= limit:
                    count += 1
                    i += 1
                i += 1
            
            return count

        left = 0
        right = nums[-1]
        while left <= right:
            mid = (left + right) // 2
            if countPairs(nums, mid) >= p:
                right = mid - 1
            else:
                left = mid + 1

        return left