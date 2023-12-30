class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        memo = [0] * 26
        count = 0
        n = len(words)
        for word in words:
            for char in word:
                index = ord(char) - ord('a')
                memo[index] += 1
                count += 1
        if count % n != 0:
            return False
        for i in range(26):
            if memo[i] % n != 0:
                return False
        return True