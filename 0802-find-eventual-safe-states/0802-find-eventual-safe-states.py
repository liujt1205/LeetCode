class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdegree = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for neighbor in graph[i]:
                adj[neighbor].append(i)
                outdegree[i] += 1

        queue = deque()
        res = []
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)

        safe = [False] * n
        while queue:
            node = queue.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    queue.append(neighbor)

        for i in range(n):
            if safe[i]:
                res.append(i)

        return res
        