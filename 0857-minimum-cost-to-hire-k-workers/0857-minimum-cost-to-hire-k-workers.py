class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = float('inf')
        qua = 0
        workers = []
        for i in range(len(quality)):
            curQ = quality[i]
            curW = wage[i]
            workers.append((curW/curQ, curQ))
        workers.sort()
        qualities = []
        for i in range(len(quality)):
            heapq.heappush(qualities, -workers[i][1])
            qua += workers[i][1]
            if len(qualities) > k:
                qua += heapq.heappop(qualities)
            if len(qualities) == k:
                res = min(res, workers[i][0] * qua)
        return res