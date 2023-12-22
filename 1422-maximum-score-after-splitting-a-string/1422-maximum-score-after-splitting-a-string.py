class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = 0
        best = -inf
        for i in range(len(s) - 1):
            if s[i] == '0':
                zero += 1
            else:
                one += 1
            best = max(best, zero - one)
        if s[-1] == '1':
            one += 1
        return best + one