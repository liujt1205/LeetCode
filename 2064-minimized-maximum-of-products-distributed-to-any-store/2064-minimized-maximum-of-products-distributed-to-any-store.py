class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        
        queue = []
        for q in quantities:
            queue.append((-q, q, 1))
            
        heapq.heapify(queue)
            
        for _ in range(n - m):
            _, total, count = heapq.heappop(queue)
            newMax = total / (count + 1)
            heapq.heappush(queue, (-newMax, total, count + 1))
            
        _, total, count = heapq.heappop(queue)
        return math.ceil(total / count)