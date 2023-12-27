class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        memo = [0] * 5
        for char in text:
            if char == 'a':
                memo[0] += 1
            elif char == 'b':
                memo[1] += 1
            elif char == 'l':
                memo[2] += 1
            elif char == 'o':
                memo[3] += 1
            elif char == 'n':
                memo[4] += 1
        res = inf
        freq = [1, 1, 2, 2, 1]
        for i in range(5):
            res = min(res, (memo[i] // freq[i]))
        return res
        