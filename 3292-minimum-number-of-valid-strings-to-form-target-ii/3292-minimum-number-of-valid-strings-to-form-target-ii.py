class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        def prefix_function(s):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                j = pi[i - 1]
                while j > 0 and s[i] != s[j]:
                    j = pi[j - 1]
                if s[i] == s[j]:
                    j += 1
                pi[i] = j
            return pi
        
        m = len(target)
        dp = [0] * m

        for w in words:
            n = len(w)
            # Calculate the prefix function for the combined string `w + '#' + t`
            p = prefix_function(w + '#' + target)
            # Update the dp array with the longest matching suffix lengths
            for i in range(m):
                dp[i] = max(dp[i], p[i + n + 1])

        m -= 1
        a = 0
        # Count the minimum number of substrings to cover the target string `t`
        while m >= 0 and dp[m] > 0:
            m -= dp[m]
            a += 1

        return a if m == -1 else -1
        