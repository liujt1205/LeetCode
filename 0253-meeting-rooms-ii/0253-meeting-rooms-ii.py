class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        heap = []
        for meeting in intervals:
            [start, stop] = meeting
            while len(heap) != 0 and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, stop)
            res = max(res, len(heap))
        return res