class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)
        for c in citations:
            count[min(n, c)] += 1

        h = n
        s = count[n]
        while h > s:
            h -= 1
            s += count[h]

        return h