class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        res = [['.'] * m for _ in range(n)]
        for row in range(m):
            count = 0
            for col in range(n):
                if box[row][col] == '#':
                    count += 1
                elif box[row][col] == '*':
                    res[col][m - 1 - row] = '*'
                    for i in range(count):
                        res[col - i - 1][m - 1 - row] = '#'
                    count = 0
                else:
                    continue
            for i in range(count):
                res[n - 1 - i][m - 1 - row] = '#'
                    
        return res