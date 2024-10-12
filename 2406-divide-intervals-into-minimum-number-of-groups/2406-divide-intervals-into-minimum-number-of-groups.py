class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        pq = []
        for left, right in intervals:
            if pq and left > pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, right)
            
        return len(pq)