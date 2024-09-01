class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        res = [[0] * n for _ in range(m)]
        for index in range(len(original)):
            row = index // n
            col = index % n
            res[row][col] = original[index]
        return res