class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        size = 0
        pq = []
        for key, value in freq.items():
            size += 1
            heapq.heappush(pq, value)
        while k > 0:
            cur = heapq.heappop(pq)
            k -= cur
            size -= 1
        return size + (k < 0)