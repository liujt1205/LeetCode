class Solution:
    class UnionFind:
            def __init__(self, size):
                self.memo = [-1] * size
                self.count = 0
                
            def is_land(self, index):
                return self.memo[index] >= 0
            
            def number_of_islands(self):
                return self.count
            
            def add_land(self, index):
                if self.memo[index] == -1:
                    self.memo[index] = index
                    self.count += 1
                    
            def find(self, index):
                if self.memo[index] != index:
                    self.memo[index] = self.find(self.memo[index])
                return self.memo[index]
                
            def union(self, first, second):
                first_root = self.find(first)
                second_root = self.find(second)
                if first_root != second_root:
                    if first_root < second_root:
                        self.memo[second_root] = first_root
                    elif first_root > second_root:
                        self.memo[first_root] = second_root
                    self.count -= 1
                    
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]    
        grid = self.UnionFind(m * n)
        res = []
        for row, col in positions:
            index = row * n + col
            grid.add_land(index)
            for i, j in neighbors:
                newRow = row + i
                newCol = col + j
                newIndex = newRow * n + newCol
                if 0 <= newRow < m and 0 <= newCol < n and grid.is_land(newIndex):
                    grid.union(index, newIndex)
            res.append(grid.number_of_islands())
        return res
            
            
            
            
            
            
            
            
            
            
            
            