class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        
        if n == 1:
            return 1
        
        left = 0
        right = n - 1
        while left < right and s[left] == s[right]:
            cur = s[left]
            while left <= right and s[left] == cur:
                left += 1
            while left < right and s[right] == cur:
                right -= 1
        return right - left + 1
        
        