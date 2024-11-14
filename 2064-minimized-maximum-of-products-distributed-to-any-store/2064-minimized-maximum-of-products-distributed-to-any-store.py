class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        biggest = max(quantities)
        left, right = 1, biggest
        while left <= right:
            mid = left + (right - left) // 2
            count = 0
            for num in quantities:
                count += num // mid + 1 - (num % mid == 0)

            if count <= n:
                right = mid - 1
            else:
                left = mid + 1
                
        return left