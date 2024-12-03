class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        chars = list(s)
        counts = [0] * 26
        max_unique = 0
        for char in chars:
            if counts[ord(char) - ord('a')] == 0:
                max_unique += 1
            counts[ord(char) - ord('a')] += 1
        
        res = 0
        for cur in range(max_unique + 1):
            counts = [0] * 26
            left, right, unique, count = 0, 0, 0, 0
            while right < len(s):
                if unique <= cur:
                    idx = ord(s[right]) - ord('a')
                    if counts[idx] == 0:
                        unique += 1
                    counts[idx] += 1
                    if counts[idx] == k:
                        count += 1
                    right += 1
                else:
                    idx = ord(s[left]) - ord('a')
                    if counts[idx] == k:
                        count -= 1
                    counts[idx] -= 1
                    if counts[idx] == 0:
                        unique -= 1
                    left += 1
                if unique == cur and unique == count:
                    res = max(res, right - left)
                    
        return res