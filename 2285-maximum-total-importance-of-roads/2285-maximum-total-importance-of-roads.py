class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        freq = [0] * n
        for a, b in roads:
            freq[a] += 1
            freq[b] += 1
        freq.sort()
        res = 0
        for num in range(n):
            res += (num + 1) * freq[num]
        
        return res