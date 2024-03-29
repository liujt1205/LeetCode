class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        count = 0
        freq = defaultdict(int)
        left = 0
        for i in range(len(s)):
            freq[s[i]] += 1
            if freq[s[i]] == 1:
                count += 1
            while count > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    count -= 1
                left += 1
            res = max(res, i - left + 1)
        return res