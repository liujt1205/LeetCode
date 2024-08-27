class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(dict)
        for i in range(len(edges)):
            start, end = edges[i]
            graph[start][end] = succProb[i]
            graph[end][start] = succProb[i]
            
        memo = [-2] * n
        
        pq = [(-1, start_node)]
        while pq:
            prob, node = heapq.heappop(pq)
            if memo[node] != -2:
                continue
            else:
                if node == end_node:
                    return -prob
                memo[node] = prob
                for neighbor in graph[node]:
                    heapq.heappush(pq, (prob * graph[node][neighbor], neighbor))
        return 0