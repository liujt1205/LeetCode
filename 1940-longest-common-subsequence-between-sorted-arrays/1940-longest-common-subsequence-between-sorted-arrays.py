class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        res = []
        freq = defaultdict(int)
        n = len(arrays)
        limit = float('inf')
        for i in range(n):
            limit = min(limit, arrays[i][-1])
        
        for i in range(n):
            index = 0
            while index < len(arrays[i]) and arrays[i][index] <= limit:
                freq[arrays[i][index]] += 1
                index += 1
        
                
        for num in freq.keys():
            if freq[num] == n:
                res.append(num)
                
        return res
            