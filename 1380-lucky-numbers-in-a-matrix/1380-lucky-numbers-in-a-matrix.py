class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        
        overall_min_max = -float('inf')
        for i in range(n):
            roll_min = min(matrix[i])
            overall_min_max = max(overall_min_max, roll_min)
            
        overall_max_min = float('inf')
        for i in range(m):
            col_max = max(matrix[j][i] for j in range(n))
            overall_max_min = min(overall_max_min, col_max)
            
        if overall_min_max == overall_max_min:
            return [overall_max_min]
        else:
            return []