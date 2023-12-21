class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(1, numRows):
            new = [1]
            for j in range(i - 1):
                new.append(res[i - 1][j] + res[i - 1][j + 1])
            new.append(1)
            res.append(new)
        return res