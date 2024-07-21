class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def getOrder(conditions, orderDict, k):
            indegree = [0] * (k + 1)
            posBelow = defaultdict(list)
            for above, below in conditions:
                posBelow[above].append(below)
                indegree[below] += 1
            queue = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    queue.append(i)
            pos = 0
            while queue:
                cur = queue.popleft()
                orderDict[cur] = pos
                pos += 1
                for below in posBelow[cur]:
                    indegree[below] -= 1
                    if indegree[below] == 0:
                        queue.append(below)
            return pos == k
        
        rowOrder, colOrder = defaultdict(list), defaultdict(list)
        if getOrder(rowConditions, rowOrder, k) and getOrder(colConditions, colOrder, k):
            res = [[0] * k for _ in range(k)]
            for i in range(1, k + 1):
                res[rowOrder[i]][colOrder[i]] = i
            return res
        else:
            print(list(rowOrder))
            print(list(colOrder))
            return []