class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        pq = []
        res = 0
        lastDay = max(event[1] for event in events)
        events.sort()
        i = 0
        for d in range(1, lastDay + 1):
            while i < len(events) and events[i][0] <= d:
                heapq.heappush(pq, events[i][1])
                i += 1
            while pq and pq[0] < d:
                heapq.heappop(pq)
            
            if pq:
                res += 1
                heapq.heappop(pq)

        return res