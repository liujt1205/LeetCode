class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        res = 0
        row = [0] * len(rooks)
        col = [0] * len(rooks)
        for rook in rooks:
            row[rook[0]] += 1
            col[rook[1]] += 1
        
        row_moves = 0
        col_moves = 0
        for i in range(len(rooks)):
            row_moves += row[i] - 1
            col_moves += col[i] - 1
            res += abs(row_moves) + abs(col_moves)
            
        return res