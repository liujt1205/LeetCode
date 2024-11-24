class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count = 0
        smallest = float('inf')
        res = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                num = matrix[row][col]
                if num < 0:
                    neg_count += 1
                smallest = min(smallest, abs(num))
                res += abs(num)
                
        if neg_count % 2 != 0:
            res -= 2 * smallest
            
        return res
        