class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def getAll(word, k):
            counter = Counter()
            j = 0
            res = 0
            for i in range(len(word)):
                if word[i] in "aeiou":
                    counter[word[i]] += 1
                else:
                    counter['_'] += 1
                while counter['a'] > 0 and counter['e'] > 0 and counter['i'] > 0 and counter['o'] > 0 and counter['u'] > 0 and counter['_'] >= k:
                    if word[j] in "aeiou":
                        counter[word[j]] -= 1
                    else:
                        counter['_'] -= 1
                    j += 1
                res += j
            return res
        
        return getAll(word, k) - getAll(word, k + 1)