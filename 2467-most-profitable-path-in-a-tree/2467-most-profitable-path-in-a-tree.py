class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        seen = [0] * n

        def dfs(i, d0):
            seen[i] = 1
            res = -inf
            db = 0 if i == bob else n
            for j in graph[i]:
                if seen[j]:
                    continue
                cur, dist = dfs(j, d0 + 1)
                res = max(res, cur)
                db = min(db, dist)
            if res == -inf:
                res = 0
            if db == d0:
                res += amount[i] // 2
            if db > d0:
                res += amount[i]
            return res, db + 1

        return dfs(0, 0)[0]