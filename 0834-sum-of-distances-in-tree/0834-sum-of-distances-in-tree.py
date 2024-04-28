class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0] * n
        graph = defaultdict(set)
        count = [1] * n
        for first, second in edges:
            graph[first].add(second)
            graph[second].add(first)
            
        def dfs(root, pre):
            for i in graph[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in graph[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + n - count[i]
                    dfs2(i, root)
                    
        dfs(0, -1)
        dfs2(0, -1)
        
        return res