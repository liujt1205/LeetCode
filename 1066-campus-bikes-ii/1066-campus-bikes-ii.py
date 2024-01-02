class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def findDistance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
        
        h = [[0, 0, 0]]
        seen = set()
        while True:
            cost, i, taken = heapq.heappop(h)
            if (i, taken) in seen: continue
            seen.add((i, taken))
            if i == len(workers):
                return cost
            for j in range(len(bikes)):
                if taken & (1 << j) == 0:
                    heapq.heappush(h, [cost + findDistance(workers[i], bikes[j]), i + 1, taken | (1 << j)])