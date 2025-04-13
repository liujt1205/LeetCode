class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]
        res = n
        def find(x):
            nonlocal root
            if root[x] != x:
                root[x] = find(root[x])

            return root[x]

        def union(x, y):
            nonlocal res
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            elif rootX > rootY:
                root[rootX] = rootY
                res -= 1
            else:
                root[rootY] = rootX
                res -= 1
        
        for a, b in edges:
            union(a, b)

        return res