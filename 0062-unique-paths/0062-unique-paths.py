class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * (n + 1)
        cur = [0] * (n + 1)
        cur[1] = 1
        for i in range(m):
            for j in range(n):
                cur[j + 1] += prev[j + 1] + cur[j]
            prev = cur
            cur = [0] * (n + 1)
            
        return prev[n]
        