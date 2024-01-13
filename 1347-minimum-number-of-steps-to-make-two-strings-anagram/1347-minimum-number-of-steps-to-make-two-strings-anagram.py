class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        sCount = Counter(s)
        tCount = Counter(t)
        for i in range(26):
            curChar = chr(ord('a') + i)
            count1 = sCount.get(curChar, 0)
            count2 = tCount.get(curChar, 0)
            if count1 > count2:
                res += count1 - count2
        return res