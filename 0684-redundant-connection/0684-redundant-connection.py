class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges) + 1)]
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
            if rootA != rootB:
                if rootA > rootB:
                    root[rootA] = rootB
                else:
                    root[rootB] = rootA
            else:
                return [a, b]
