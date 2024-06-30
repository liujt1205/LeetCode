class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        Alice = UnionFind(n)
        Bob = UnionFind(n)
        edges.sort(key = lambda edge: edge[0], reverse = True)
        for edge in edges:
            edgeType, start, end = edge
            if edgeType == 3:
                if not Alice.check(start, end):
                    Alice.Union(start, end)
                    Bob.Union(start, end)
                else:
                    res += 1
            elif edgeType == 1:
                if not Alice.check(start, end):
                    Alice.Union(start, end)
                else:
                    res += 1
            elif edgeType == 2:
                if not Bob.check(start, end):
                    Bob.Union(start, end)
                else:
                    res += 1
        if Alice.allConnected() and Bob.allConnected():
            return res
        else:
            return -1
        
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]
    
    def find(self, index):
        if self.root[index] == index:
            return index
        self.root[index] = self.find(self.root[index])
        return self.root[index]
    
    def check(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        return rootX == rootY
    
    def Union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX < rootY:
            self.root[rootY] = rootX
        else:
            self.root[rootX] = rootY
    
    def allConnected(self):
        for i in range(2, len(self.root)):
            if self.root[i] == i:
                return False
        return True