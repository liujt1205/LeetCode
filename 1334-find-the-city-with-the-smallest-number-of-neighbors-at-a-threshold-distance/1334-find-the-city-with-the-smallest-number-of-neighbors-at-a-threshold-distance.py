class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances = [[float('inf')] * n for _ in range(n)]
        for i, j, d in edges:
            distances[i][j] = d
            distances[j][i] = d
        for i in range(n):
            distances[i][i] = 0
        for mid in range(n):
            for start in range(n):
                for end in range(n):
                    distances[start][end] = min(distances[start][end], distances[start][mid] + distances[mid][end])
        count = [0] * n
        for i in range(n):
            for j in range(n):
                if distances[i][j] <= distanceThreshold:
                    count[i] += 1
        minCount = float('inf')
        res = -1
        for i in range(n):
            if count[i] <= minCount:
                res = i
                minCount = count[i]
        return res