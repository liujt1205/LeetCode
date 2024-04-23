class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        graph = [set() for i in range(n)]
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
            
        queue = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                queue.append(i)
        remaining = n
        while remaining > 2:
            remaining -= len(queue)
            for _ in range(len(queue)):
                cur = queue.popleft()
                root = graph[cur].pop()
                graph[root].remove(cur)
                if len(graph[root]) == 1:
                    queue.append(root)
        
        return queue