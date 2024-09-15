class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        start = {0: -1}
        mask = 0
        vowels = {'a': 1 << 4, 'e': 1 << 3, 'i': 1 << 2, 'o': 1 << 1, 'u': 1}
        res = 0
        
        for i in range(len(s)):
            if s[i] in vowels:
                mask ^= vowels[s[i]]
            
            if mask in start:
                res = max(res, i - start[mask])
            else:
                start[mask] = i
            
        return res
                    