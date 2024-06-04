class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        res = 0
        odd = False
        for char in freq.keys():
            res += freq[char] - freq[char] % 2
            if not odd and freq[char] % 2 != 0:
                odd = True
        if odd:
            res += 1
        return res