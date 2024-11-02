class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        count = [[0] * 26 for _ in range(len(s) + 1)]
        for i in range(len(s)):
            for j in range(26):
                count[i + 1][j] = count[i][j]
            count[i + 1][ord(s[i]) - ord('a')] += 1
            
        res = []
        for start, end in queries:
            cur = 0
            for i in range(26):
                curCount = count[end + 1][i] - count[start][i]
                cur += (1 + curCount) * curCount // 2
                
            res.append(cur)
        
        return res