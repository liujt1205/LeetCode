class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        cap = max(nums)
        exist = [False] * (cap + 1)
        for num in nums:
            exist[num] = True
        if exist[1]:
            return False
        sieve = [0] * (cap + 1)
        i = 2
        while i <= cap:
            if sieve[i] == 0:
                for j in range(i, cap + 1, i):
                    sieve[j] = i
            i += 1
        graph = UnionFind(cap * 2 + 1)
        for num in nums:
            val = num
            while val > 1:
                prime = sieve[val]
                anchor = cap + prime
                if not graph.check(num, anchor):
                    graph.union(num, anchor)
                while val % prime == 0:
                    val = val // prime
        count = 0
        for k in range(2, cap + 1):
            if exist[k] and graph.find(k) == k:
                count += 1
        return count == 1
        
        
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px                
            self.parent[py] = px
            self.size[px] += self.size[py]
    
    def check(self, x, y):
        return self.find(x) == self.find(y)
