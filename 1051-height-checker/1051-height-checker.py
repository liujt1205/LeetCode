class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = defaultdict(int)
        for num in heights:
            count[num] += 1
        minH, maxH = min(heights), max(heights)
        correct = []
        for i in range(minH, maxH + 1):
            while count[i] > 0:
                correct.append(i)
                count[i] -= 1
        res = 0
        for i in range(len(heights)):
            if heights[i] != correct[i]:
                res += 1
        return res