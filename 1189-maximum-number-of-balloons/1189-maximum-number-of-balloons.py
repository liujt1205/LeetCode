class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        memo = [0] * 26
        for char in text:
            index = ord(char) - ord('a')
            memo[index] += 1
        res = inf
        check = ['a', 'b', 'l', 'o', 'n']
        freq = [1, 1, 2, 2, 1]
        for i in range(5):
            index = ord(check[i]) - ord('a')
            res = min(res, (memo[index] // freq[i]))
        return res
        