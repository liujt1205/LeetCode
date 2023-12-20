class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                summ = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if i + k >= 0 and i + k < m and l + j >= 0 and l + j < n:
                            count += 1
                            summ += img[i + k][j + l]
                res[i][j] = summ // count
        return res