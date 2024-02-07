class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        pq = []
        for char, freq in counter.items():
            heapq.heappush(pq, (-freq, char))
        res = ""
        while pq:
            freq, char = heapq.heappop(pq)
            res += char * (-freq)
        return res