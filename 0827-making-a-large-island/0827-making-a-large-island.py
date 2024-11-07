class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        if 0 <= row + d[0] < n and 0 <= col + d[1] < n and grid[row + d[0]][col + d[1]] == 1:
                            uf.union((row * n + col), ((row + d[0]) * n + col + d[1]))
        
        res = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    res = max(res, uf.unionNeighbor(row * n + col, grid))
                    
        return res if res else n * n
        
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.size = [1] * n * n
        self.root = [i for i in range(n * n)]
        
    def find(self, index):
        if self.root[index] == index:
            return index
        
        self.root[index] = self.find(self.root[index])
        return self.root[index]
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return
        elif rootA < rootB:
            self.root[rootB] = rootA
            self.size[rootA] += self.size[rootB]
            
    def unionNeighbor(self, index, board):
        res = 1
        seen = set()
        if index % self.n != 0:
            neighbor = index - 1
            if board[neighbor // self.n][neighbor % self.n] == 1:
                root = self.find(neighbor)
                if root not in seen:
                    res += self.size[root]
                    seen.add(root)
        if index >= self.n:
            neighbor = index - self.n
            if board[neighbor // self.n][neighbor % self.n] == 1:
                root = self.find(neighbor)
                if root not in seen:
                    res += self.size[root]
                    seen.add(root)
        if (index + 1) % self.n != 0:
            neighbor = index + 1
            if board[neighbor // self.n][neighbor % self.n] == 1:
                root = self.find(neighbor)
                if root not in seen:
                    res += self.size[root]
                    seen.add(root)
        if index < self.n * (self.n - 1):
            neighbor = index + self.n
            if board[neighbor // self.n][neighbor % self.n] == 1:
                root = self.find(neighbor)
                if root not in seen:
                    res += self.size[root]
                    seen.add(root)
        
        return res
            
            