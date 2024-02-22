class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        n = len(edges) + 1
        graph = [set() for _ in range(n)]
        for edge in edges:
            first, second = edge
            graph[first].add(second)
            graph[second].add(first)
        def findDistance(node, n):
            queue = deque([node])
            distance = -1
            visited = [0] * n
            visited[node] = 1
            lastNode = node
            while queue:
                next_queue = deque()
                while queue:
                    cur = queue.popleft()
                    for neighbor in graph[cur]:
                        if visited[neighbor] == 0:
                            visited[neighbor] = 1
                            next_queue.append(neighbor)
                            lastNode = neighbor
                distance += 1
                queue = next_queue
            return distance, lastNode
        
        dis, far = findDistance(0, n)
        res, realFar = findDistance(far, n)
        return res
        