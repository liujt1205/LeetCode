class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        res = max(vals)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(-vals[b])
            graph[b].append(-vals[a])
            
        for node in graph:
            cur = vals[node]
            heapq.heapify(graph[node])
            edge = 0
            while edge < k and graph[node]:
                edge += 1
                biggest = -heapq.heappop(graph[node])
                if biggest < 0:
                    break
                cur += biggest
            res = max(res, cur)
            
        return res
            
        