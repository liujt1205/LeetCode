class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        def calSum(l, r):
            count = min(books[r], r - l + 1)
            return (2 * books[r] - (count - 1)) * count // 2
        stack = []
        dp = [0] * n
        for i in range(n):
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()
            if not stack:
                dp[i] = calSum(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + calSum(j + 1, i)
            stack.append(i)
        return max(dp)