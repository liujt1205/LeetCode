class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        queue = []
        maxProfit = 0
        for i in range(len(jobs)):
            start, end, profit = jobs[i]
            while len(queue) != 0 and queue[0][0] <= start:
                maxProfit = max(maxProfit, queue[0][1])
                heapq.heappop(queue)
            heapq.heappush(queue, [end, maxProfit + profit])
        while len(queue) != 0:
            maxProfit = max(maxProfit, queue[0][1])
            heapq.heappop(queue)
        return maxProfit