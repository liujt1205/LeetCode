class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = [0]
        def getMax(root, parent):
            children = []
            for node in graph[root]:
                if node == parent:
                    continue
                children.append(getMax(node, root))

            if len(children) == 0:
                return cost[root]

            maxChild = max(children)
            res[0] += sum(maxChild - score > 0 for score in children)
            
            return maxChild + cost[root]

        getMax(0, -1)
        return res[0]
