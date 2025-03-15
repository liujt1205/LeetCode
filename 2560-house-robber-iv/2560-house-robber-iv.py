class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = 1, max(nums)
        n = len(nums)

        while left < right:
            mid = (left + right) // 2
            count = 0

            index = 0
            while index < n:
                if nums[index] <= mid:
                    count += 1
                    index += 2
                else:
                    index += 1

            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left
