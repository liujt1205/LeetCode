class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        graph = defaultdict(list)
        for start, end in pairs:
            indegree[end] += 1
            outdegree[start] += 1
            graph[start].append(end)
            
        startNode = pairs[0][0]
        for node in outdegree:
            if indegree[node] + 1 == outdegree[node]:
                startNode = node
                break
                
        res = []
                
        stack = [startNode]
        while stack:
            cur = stack[-1]
            if graph[cur]:
                nextNode = graph[cur].pop(0)
                stack.append(nextNode)
            else:
                res.append(cur)
                stack.pop()
        res.reverse()
                
        res_pairs = []
        for i in range(1, len(res)):
            res_pairs.append([res[i - 1], res[i]])
            
        return res_pairs
            