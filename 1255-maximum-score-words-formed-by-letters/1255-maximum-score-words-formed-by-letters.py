class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = [0] * 26
        for letter in letters:
            count[ord(letter) - ord('a')] += 1
        def calSet(wordSet, count, score):
            res = 0
            tempCount = [0] * 26
            for word in wordSet:
                for char in word:
                    index = ord(char) - ord('a')
                    tempCount[index] += 1
                    res += score[index]
            for i in range(26):
                if tempCount[i] > count[i]:
                    return 0
            return res
        
        wordSet = [[]]
        res = 0
        for word in words:
            tempList = []
            for i in range(len(wordSet)):
                temp = wordSet[i][:]
                temp.append(word)
                tempList.append(temp)
            wordSet.extend(tempList)
        for words in wordSet:
            res = max(res, calSet(words, count, score))
        return res