class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            mid = left + (right - left) // 2
            count = 0
            for num in nums:
                if num > mid:
                    count += ceil(num / mid) - 1
                    
            if count > maxOperations:
                left = mid + 1
            else:
                right = mid - 1
                
        return left