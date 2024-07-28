class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque()
        queue.append((1, 0))
        visited = [[-1, -1] for _ in range(n + 1)]
        visited[1][0] = 0
        while queue:
            vertex, arriveTime = queue.popleft()
            print(vertex, arriveTime, visited[n])
            if vertex == n and visited[n][1] != -1:
                return visited[n][1]
            if (arriveTime // change) % 2 != 0:
                arriveTime += change - arriveTime % change
            arriveTime += time
            for neighbor in graph[vertex]:
                if visited[neighbor][0] == -1:
                    visited[neighbor][0] = arriveTime
                    queue.append((neighbor, arriveTime))
                elif visited[neighbor][1] == -1 and arriveTime != visited[neighbor][0]:
                    visited[neighbor][1] = arriveTime
                    queue.append((neighbor, arriveTime))

        return -1
        