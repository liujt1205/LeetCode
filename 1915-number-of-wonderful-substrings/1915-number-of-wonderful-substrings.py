class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1
        res = cur = 0
        for char in word:
            cur ^= 1 << ord(char) - ord('a')
            res += count[cur]
            for i in range(10):
                res += count[cur ^ (1 << i)]
            count[cur] += 1
        return res