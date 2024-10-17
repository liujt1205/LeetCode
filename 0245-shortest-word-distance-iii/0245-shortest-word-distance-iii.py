class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        prev1 = None
        prev2 = None
        res = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word == word1:
                if prev2 is not None:
                    res = min(res, i - prev2)
                prev1 = i
                if word1 == word2:
                    prev2 = i
            elif word == word2:
                if prev1 is not None:
                    res = min(res, i - prev1)
                prev2 = i
                
        return res