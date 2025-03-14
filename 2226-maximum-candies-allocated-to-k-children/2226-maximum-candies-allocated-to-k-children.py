class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, max(candies)
        while left < right:
            target = (left + right) // 2 + 1
            count = 0
            for pile in candies:
                count += pile // target
            
            if count >= k:
                left = target
            else:
                right = target - 1

        return left