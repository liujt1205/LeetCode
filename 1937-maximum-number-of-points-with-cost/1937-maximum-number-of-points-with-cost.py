class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        cur_row = [0] * n
        pre_row = [0] * n
        for row in points:
            cur_max = 0
            for col in range(n):
                cur_max = max(cur_max - 1, pre_row[col])
                cur_row[col] = cur_max
                
            cur_max = 0
            for col in range(n - 1, -1 , -1):
                cur_max = max(cur_max - 1, pre_row[col])
                cur_row[col] = max(cur_row[col], cur_max) + row[col]
            
            pre_row = cur_row.copy()
            
        return max(pre_row)