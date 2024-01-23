class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forb = set(forbidden)
        res = 0
        curStr = ""
        curLeng = 0
        for i in range(len(word) - 1, -1, -1):
            curStr = word[i] + curStr
            curLeng += 1
            for i in range(min(10, curLeng)):
                if curStr[:i + 1] in forb:
                    res = max(res, curLeng - 1)
                    curStr = curStr[:i]
                    curLeng = len(curStr)
                    break
        res = max(res, curLeng)
        return res