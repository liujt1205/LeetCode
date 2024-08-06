class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        sorted_count = sorted(count.items(), key=lambda x: -x[1])
        res = 0
        for i in range(len(sorted_count)):
            res += sorted_count[i][1] * (i // 8 + 1)
        return res