class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = {}
        memo[""] = 0
        res = 0
        sortedWords = sorted(words, key=lambda s: (len(s), s))
        for word in sortedWords:
            length = 1
            for i in range(len(word)):
                if i == 0:
                    key = word[1:]
                elif i == len(word) - 1:
                    key = word[:i]
                else:
                    key = word[:i] + word[i+1:]
                if memo.get(key, 0):
                    length = max(length, memo[key] + 1)
            memo[word] = length
            res = max(res, length)
        return res