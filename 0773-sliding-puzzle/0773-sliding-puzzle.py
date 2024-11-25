class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ""
        for row in range(2):
            for col in range(3):
                start += str(board[row][col])
        target = "123450"
        queue = deque([target])
        dirs = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        visited = set()
        visited.add(target)
        move = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                cur_state = queue.popleft()
                if cur_state == start:
                    return move
                index = cur_state.index('0')
                for new_index in dirs[index]:
                    state = list(cur_state)
                    state[index], state[new_index] = state[new_index], state[index]
                    new_state = "".join(state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
            move += 1
            
        return -1