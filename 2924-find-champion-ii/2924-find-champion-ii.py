class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for a, b in edges:
            indegree[b] += 1
            
        count = 0
        res = -1
        for i in range(n):
            if indegree[i] == 0:
                count += 1
                res = i
                if count > 1:
                    return -1
                    
        return res