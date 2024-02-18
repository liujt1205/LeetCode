class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = [i for i in range(n)]
        ongoing = []
        count = [0] * n
        meetings.sort()
        i = 0
        for meeting in meetings:
            start, end = meeting
            while ongoing and start >= ongoing[0][0]:
                time, room = heapq.heappop(ongoing)
                heapq.heappush(available, room)
            if available:
                room = heapq.heappop(available)
                heapq.heappush(ongoing, (end, room))
                count[room] += 1
            else:
                time, room = heapq.heappop(ongoing)
                heapq.heappush(ongoing, (end - start + time, room))
                count[room] += 1
        maxCount = 0     
        res = -1
        for i in range(n):
            if count[i] > maxCount:
                res = i
                maxCount = count[i]
        return res