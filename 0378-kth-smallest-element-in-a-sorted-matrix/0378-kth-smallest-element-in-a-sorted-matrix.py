class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = []
        for i in range(min(n, k)):
            pq.append((matrix[i][0], i, 0))
            
        heapq.heapify(pq)
        while k > 0:
            cur, row, col = heapq.heappop(pq)
            if col < n - 1:
                heapq.heappush(pq, (matrix[row][col + 1], row, col + 1))
            k -= 1
            
        return cur