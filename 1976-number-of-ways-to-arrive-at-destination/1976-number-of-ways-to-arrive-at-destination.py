class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        MOD = 1000000007
        for u, v, t in roads:
            graph[u][v] = t
            graph[v][u] = t

        pq = [(0, 0)]
        shortest_time = [float("inf")] * n
        path_count = [0] * n

        shortest_time[0] = 0
        path_count[0] = 1

        while pq:
            curr_time, cur = heapq.heappop(pq)
            if curr_time > shortest_time[cur]:
                continue

            for neighbor in graph[cur]:
                cost = graph[cur][neighbor]
                if curr_time + cost < shortest_time[neighbor]:
                    shortest_time[neighbor] = curr_time + cost
                    path_count[neighbor] = path_count[cur]
                    heapq.heappush(pq, (shortest_time[neighbor], neighbor))

                elif curr_time + cost == shortest_time[neighbor]:
                    path_count[neighbor] = (
                        path_count[neighbor] + path_count[cur]
                    ) % MOD

        return path_count[n - 1]