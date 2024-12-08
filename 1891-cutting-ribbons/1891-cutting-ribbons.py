class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if sum(ribbons) < k:
            return 0
        shortest, longest = 1, max(ribbons)
        while shortest <= longest:
            mid = shortest + (longest - shortest) // 2
            count = 0
            for ribbon in ribbons:
                count += ribbon // mid
                if count > k:
                    break
                
            if count >= k:
                shortest = mid + 1
            else:
                longest = mid - 1
                
        return longest
        