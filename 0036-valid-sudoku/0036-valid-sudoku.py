class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    num = ord(cur) - ord('1')
                    if rows[i][num] or cols[j][num] or boxes[(i // 3) * 3 + j // 3][num]:
                        return False
                    else:
                        rows[i][num] = 1
                        cols[j][num] = 1
                        boxes[(i // 3) * 3 + j // 3][num] = 1
        return True