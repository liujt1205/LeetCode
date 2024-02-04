class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        freq = {}
        res = ""
        count = 0
        length = float('inf')
        for char in t:
            if freq.get(char, 0) == 0:
                count += 1
            freq[char] = freq.get(char, 0) - 1
        while right < len(s):
            cur = s[right]
            if cur in freq:
                freq[cur] += 1
                if freq[cur] == 0:
                    count -= 1
                while count == 0:
                    if right - left < length:
                        res = s[left: right + 1]
                        length = right - left
                    pre = s[left]
                    if pre in freq:
                        freq[pre] -= 1
                        if freq[pre] < 0:
                            count += 1
                    left += 1
            right += 1
        return res
                