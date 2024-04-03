class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(board, word, row, col, i):
            if i == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[i]:
                return False
            cur = board[row][col]
            board[row][col] = '#'
            if helper(board, word, row+1, col, i+1) or helper(board, word, row-1, col, i+1) or helper(board, word, row, col+1, i+1) or helper(board, word, row, col-1, i+1):
                return True
            board[row][col] = cur
            return False
                
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if helper(board, word, row, col, 0):
                    return True
        return False