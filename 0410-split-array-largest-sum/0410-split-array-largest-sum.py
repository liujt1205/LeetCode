class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def group(limit):
            cur = 0
            split = 0
            for num in nums:
                if cur + num <= limit:
                    cur += num
                else:
                    cur = num
                    split += 1

            return split + 1

        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if group(mid) <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left