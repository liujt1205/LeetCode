class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for (num, frequency) in freq.items():
            heapq.heappush(heap, (frequency, num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while len(heap) != 0:
            res.append(heapq.heappop(heap)[1])
        return res