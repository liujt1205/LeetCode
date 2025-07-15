class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pq = []
        for p, f, t in trips:
            pq.append((f, p))
            pq.append((t, -p))

        heapq.heapify(pq)
        cur = 0
        while pq:
            loc, p = heapq.heappop(pq)
            cur += p
            if cur > capacity:
                return False

        return True