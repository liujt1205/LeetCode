class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        root = [i for i in range(n)]
        def find(index):
            nonlocal root
            cur = index
            while root[cur] != cur:
                cur = root[cur]

            root[index] = cur
            return root[index]

        for a, b in edges:
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return False
            if rootA > rootB:
                root[rootA] = rootB
            else:
                root[rootB] = rootA

        return True