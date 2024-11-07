class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            count = 0
            for num in piles:
                count += num // mid
                if num % mid != 0:
                    count += 1
            
            if count <= h:
                right = mid - 1
            else:
                left = mid + 1
                
        return left