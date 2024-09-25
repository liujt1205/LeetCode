class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(s):
           dp = [0] * len(s)
           for i in range(1, len(s)):
               cur = dp[i - 1]
               while cur and s[i] != s[cur]:
                   cur = dp[cur - 1]
               dp[i] = cur + (s[i] == s[cur])
           return dp

        n, la, lb = len(s), len(a), len(b)
        v1 = kmp(a + '#' + s)
        v2 = kmp(b + '#' + s)
        found_a = [i - la - la for i,v in enumerate(v1) if v >= la]
        found_b = [j - lb - lb for j,v in enumerate(v2) if v >= lb]
                
        res = []
        start = 0
        for i in range(len(found_a)):
            while start < len(found_b) and found_b[start] < found_a[i] - k:
                start += 1
            if start < len(found_b) and found_b[start] <= found_a[i] + k:
                res.append(found_a[i])
                    
        return res