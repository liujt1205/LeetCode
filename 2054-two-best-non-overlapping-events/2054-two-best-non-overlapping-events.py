class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        res = 0
        max_completed = 0
        events.sort()
        pq = []
        for start, end, value in events:
            while pq and pq[0][0] < start:
                nextEnd, nextVal = heapq.heappop(pq)
                max_completed = max(max_completed, nextVal)
                
            res = max(res, max_completed + value)
            heapq.heappush(pq, (end, value))
            
        return res