class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        
        group = defaultdict(list)
        for x, y, t in meetings:
            group[t].append((x, y))
        
        graph = UnionFind(n)
        graph.union(0, firstPerson)
        
        for t in group:
            for x, y in group[t]:
                graph.union(x, y)
                
            for x, y in group[t]:
                if not graph.check(x, 0):
                    graph.reset(x)
                    graph.reset(y)
        return [i for i in range(n) if graph.check(i, 0)]
        
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[py] > self.rank[px]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1
    
    def check(self, x, y):
        return self.find(x) == self.find(y)
    
    def reset(self, x):
        self.parent[x] = x
        self.rank[x] = 0