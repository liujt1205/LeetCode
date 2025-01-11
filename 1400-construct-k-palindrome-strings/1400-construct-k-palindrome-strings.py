class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1

        odd = 0
        for i in range(26):
            if count[i] % 2 != 0:
                odd += 1

        if k >= odd and k <= n:
            return True
        
        return False