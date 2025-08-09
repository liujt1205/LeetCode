class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = {}
        left = -1
        res = 0
        for right in range(len(s)):
            if s[right] in indexes:
                left = max(left, indexes[s[right]])
                indexes[s[right]] = right
            else:
                indexes[s[right]] = right

            res = max(res, right - left)

        return res
