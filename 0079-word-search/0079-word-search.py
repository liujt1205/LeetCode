class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(board, visited, word, row, col, i):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visited[row][col] == 1 or board[row][col] != word[i]:
                return False
            visited[row][col] = 1
            if i == len(word) - 1:
                return True
            res = False
            for direction in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                newRow = row + direction[0]
                newCol = col + direction[1]
                res = res or helper(board, visited, word, newRow, newCol, i + 1)
                if res:
                    return True
            visited[row][col] = 0
            return False
                
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                visited = [[0] * len(board[0]) for _ in range(len(board))]
                if helper(board, visited, word, row, col, 0):
                    return True
        return False