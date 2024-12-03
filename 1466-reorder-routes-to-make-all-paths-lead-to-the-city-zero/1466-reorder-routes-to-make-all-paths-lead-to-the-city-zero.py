class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        dists = [float('inf')] * n
        dists[0] = 0
        graph = defaultdict(list)
        for start, end in connections:
            graph[start].append(end)
            graph[end].append(start)
            
        queue = deque([0])
        dist = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                for neighbor in graph[cur]:
                    if dists[neighbor] == float('inf'):
                        dists[neighbor] = dist + 1
                        queue.append(neighbor)
                        
            dist += 1
            
        res = 0
        for start, end in connections:
            if dists[start] < dists[end]:
                res += 1
                
        return res