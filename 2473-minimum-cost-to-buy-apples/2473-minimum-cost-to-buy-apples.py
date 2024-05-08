class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = defaultdict(list)
        for i in range(len(roads)):
            start, end, dist = roads[i]
            graph[start].append((end, dist))
            graph[end].append((start, dist))
        res = []    
        for i in range(1, n + 1):
            seen = set()
            pq = []
            heapq.heappush(pq, (0, i, False))
            while pq:
                total, city, apple = heapq.heappop(pq)
                if apple:
                    res.append(total)
                    break
                if city in seen:
                    continue
                else:
                    seen.add(city)
                    heapq.heappush(pq, (total+appleCost[city-1], city, True))
                    for neighbor, dist in graph[city]:
                        heapq.heappush(pq, (total+(1+k)*dist, neighbor, False))
        return res