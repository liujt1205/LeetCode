class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        res = 0
        left = 0
        for right in range(len(s)):
            if s[right] in lastSeen:
                left = max(left, lastSeen[s[right]])
                
            res = max(res, right - left + 1)
            lastSeen[s[right]] = right + 1
            
        return res
                