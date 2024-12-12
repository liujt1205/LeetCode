class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        neg = [-i for i in gifts]
        heapq.heapify(neg)
        while k > 0:
            cur = heapq.heappop(neg)
            after = floor(sqrt(-cur))
            heapq.heappush(neg, -after)
            k -= 1
            
        return -sum(neg)
        