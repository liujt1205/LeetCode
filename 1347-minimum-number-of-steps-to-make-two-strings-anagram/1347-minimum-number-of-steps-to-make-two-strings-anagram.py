class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        sCount = Counter(s)
        tCount = Counter(t)
        for char, count in sCount.items():
            target = tCount.get(char, 0)
            res += abs(target - count)
        for char, count in tCount.items():
            if char not in sCount:
                res += count
        return res // 2