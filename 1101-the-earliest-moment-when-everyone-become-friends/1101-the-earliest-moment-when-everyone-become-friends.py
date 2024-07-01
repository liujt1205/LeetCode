class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        union = UnionFind(n)
        count = n
        logs.sort(key=lambda x: x[0])
        for log in logs:
            time, x, y = log
            if not union.check(x, y):
                union.union(x, y)
                count -= 1
            if count == 1:
                return time
        return -1
        
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        
    def find(self, index):
        if self.root[index] == index:
            return index
        self.root[index] = self.find(self.root[index])
        return self.root[index]
    
    def check(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        return rootX == rootY
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX < rootY:
            self.root[rootY] = rootX
        else:
            self.root[rootX] = rootY