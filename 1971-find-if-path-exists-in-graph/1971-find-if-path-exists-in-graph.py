class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        visited = [False] * n
        for i in range(len(edges)):
            first, second = edges[i]
            graph[first].add(second)
            graph[second].add(first)
            
        queue = deque()
        queue.append(source)
        while queue:
            cur = queue.popleft()
            if not visited[cur]:
                visited[cur] = True
                if cur == destination:
                    return True
                queue.extend(graph[cur])
        
        return False