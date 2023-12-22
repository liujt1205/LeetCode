class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left = [0] * (n - 1)
        left[0] = s[0] == '0'
        for i in range(1, n - 1):
            change = 1 if s[i] == '0' else -1
            left[i] = left[i - 1] + change
        max = left[0]
        j = 0
        for i in range(n - 1):
            if left[i] > max:
                max = left[i]
                j = i
        right = 0
        left = 0
        for i in range(j + 1):
            if s[i] == '0':
                left += 1
        for i in range(n - 1, j, -1):
            if s[i] == '1':
                right += 1
        return left + right