class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        heap = []
        ans = grid[0][0]

        visited = [[False] * C for _ in range(R)]

        heapq.heappush(heap, (-grid[0][0], 0, 0))
        visited[0][0] = True

        while heap:
            cur_val, cur_row, cur_col = heapq.heappop(heap)

            ans = min(ans, grid[cur_row][cur_col])

            if cur_row == R - 1 and cur_col == C - 1:
                break
            for d_row, d_col in dirs:
                new_row = cur_row + d_row
                new_col = cur_col + d_col

                if (
                    0 <= new_row < R
                    and 0 <= new_col < C
                    and not visited[new_row][new_col]
                ):
                    heapq.heappush(
                        heap, (-grid[new_row][new_col], new_row, new_col)
                    )
                    visited[new_row][new_col] = True

        return ans