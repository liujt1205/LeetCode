class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])
        prefixSum = [[0] * (c + 1) for _ in range(r + 1)]
        for row in range(1, r + 1):
            for col in range(1, c + 1):
                prefixSum[row][col] = prefixSum[row - 1][col] + prefixSum[row][col - 1] - prefixSum[row - 1][col - 1] + matrix[row - 1][col - 1]
        res = 0
        for r1 in range(1, r + 1):
            for r2 in range(r1, r + 1):
                sumMap = {}
                sumMap[0] = 1
                for col in range(1, col + 1):
                    curSum = prefixSum[r2][col] - prefixSum[r1 - 1][col]
                    res += sumMap.get(curSum - target, 0)
                    sumMap[curSum] = sumMap.get(curSum, 0) + 1
        return res