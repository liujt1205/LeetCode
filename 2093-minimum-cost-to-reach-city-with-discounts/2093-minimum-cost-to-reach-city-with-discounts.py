class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = [[] for _ in range(n)]
        for x, y, toll in highways:
            graph[x].append((y, toll))
            graph[y].append((x, toll))
        
        pq = [(0, 0, 0)]
        memo = [[-1] * (discounts + 1) for _ in range(n)]
        while pq:
            dist, dest, count = heapq.heappop(pq)
            if dest == n - 1:
                return dist
            if memo[dest][count] != -1:
                continue
            else:
                memo[dest][count] = dist
            for neighbor, toll in graph[dest]:
                if memo[neighbor][count] == -1:
                    heapq.heappush(pq, (dist + toll, neighbor, count))
                    if count < discounts and memo[neighbor][count + 1] == -1:
                        heapq.heappush(pq, (dist + toll // 2, neighbor, count + 1))
        return -1