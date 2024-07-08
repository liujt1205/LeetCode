class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i + 1 for i in range(n)]
        size = n
        start = -1
        while size > 1:
            move = k % size + size
            while move > 0:
                start = (start + 1) % n
                if players[start] != 0:
                    move -= 1
            players[start] = 0
            size -= 1
        for i in range(n):
            if players[i] != 0:
                return players[i]