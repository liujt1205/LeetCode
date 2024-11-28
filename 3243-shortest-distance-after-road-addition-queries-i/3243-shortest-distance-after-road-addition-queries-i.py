class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(n, neighbors):
            visited = [False] * n
            queue = deque()
            queue.append(0)
            visited[0] = True
            
            dist = 0
            while queue:
                for _ in range(len(queue)):
                    cur = queue.popleft()
                    if cur == n - 1:
                        return dist
                    for neighbor in neighbors[cur]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True
                dist += 1
                
            return -1
            
        neighbors = [[] for _ in range(n)]
        for i in range(n - 1):
            neighbors[i].append(i + 1)
            
        res = []
        for start, end in queries:
            neighbors[start].append(end)
            res.append(bfs(n, neighbors))
            
        return res