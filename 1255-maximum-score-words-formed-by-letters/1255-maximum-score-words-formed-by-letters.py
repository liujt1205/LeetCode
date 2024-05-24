class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        count = [0] * 26
        for letter in letters:
            count[ord(letter) - ord('a')] += 1
            
        def calSet(letterCount, count, score):
            res = 0
            for i in range(26):
                if letterCount[i] > count[i]:
                    return 0
                res += letterCount[i] * score[i]
            return res
        
        res = 0
        for mask in range(1 << n):
            letterCount = [0] * 26
            valid = True
            for i in range(n):
                if mask & (1 << i):
                    for char in words[i]:
                        index = ord(char) - ord('a')
                        letterCount[index] += 1
                        if letterCount[index] > count[index]:
                            valid = False
                            break
                if not valid:
                    break
            if valid:
                res = max(res, calSet(letterCount, count, score))
            
        return res