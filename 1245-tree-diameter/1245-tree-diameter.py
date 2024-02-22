class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        graph = {}
        n = len(edges) + 1
        for edge in edges:
            first, second = edge
            graph.setdefault(first, [])
            graph[first].append(second)
            graph.setdefault(second, [])
            graph[second].append(first)
        def findDistance(node, n):
            distance = [-1] * n
            queue = deque([(node, 0)])
            while queue:
                m = len(queue)
                for i in range(m):
                    node, dis = queue.popleft()
                    if distance[node] == -1:
                        distance[node] = dis
                        for neighbor in graph[node]:
                            queue.append((neighbor, dis + 1))
            biggest = 0
            farNode = 0
            for i in range(n):
                if distance[i] > biggest:
                    farNode = i
                    biggest = distance[i]
            return biggest, farNode
        
        dis, far = findDistance(0, n)
        res, realFar = findDistance(far, n)
        return res
        