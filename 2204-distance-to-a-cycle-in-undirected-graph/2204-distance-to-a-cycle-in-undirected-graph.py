class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [float('inf')] * n
        graph = defaultdict(set)
        indegree = [0] * n
        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1
            graph[a].add(b)
            graph[b].add(a)
            
        queue = deque()
        not_in_circle = set()
        for i in range(n):
            if indegree[i] == 1:
                indegree[i] -= 1
                queue.append(i)

        while queue:
            cur = queue.popleft()
            for neighbor in graph[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    indegree[neighbor] -= 1
                    queue.append(neighbor)
                    
        for i in range(n):
            if indegree[i] > 0:
                res[i] = 0
                queue.append((i, 0))
                
        while queue:
            cur, dist = queue.popleft()
            for neighbor in graph[cur]:
                if res[neighbor] == float('inf'):
                    res[neighbor] = dist + 1
                    queue.append((neighbor, dist + 1))
                    
        return res
