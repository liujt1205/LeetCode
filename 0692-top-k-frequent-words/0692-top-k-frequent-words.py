class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        pq = []
        for word, freq in count.items():
            heappush(pq, Pair(word, freq))
            if len(pq) > k:
                heappop(pq)

        return [pair.word for pair in sorted(pq, reverse=True)]

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)