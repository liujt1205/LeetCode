class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        left = 0
        nums.sort()
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            count = 0
            start = 0
            for end in range(1, len(nums)):
                while nums[end] - nums[start] > mid:
                    start += 1
                count += end - start
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left