class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = [[] for _ in range(numRows)]
        d = 1
        i = 0
        row = 0
        for char in s:
            strings[row].append(char)
            if numRows == 1:
                d = 0
            elif row == numRows - 1:
                d = -1
            elif row == 0:
                d = 1
            row += d
                
        return ''.join([''.join(row) for row in strings])