class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for flight in flights:
            fr, to, pr = flight
            graph[fr].append((to, pr))
            
        pq = [(0, src, -1)]
        res = float('inf')
        visited = [float('inf')] * n
        while pq:
            cost, cur, stop = heapq.heappop(pq)
            if stop > k or stop > visited[cur]:
                continue
            visited[cur] = stop
            if cur == dst:
                return cost
            for neighbor, pr in graph[cur]:
                heapq.heappush(pq, (cost + pr, neighbor, stop + 1))
        if res == float('inf'):
            return -1
        return res
        
            