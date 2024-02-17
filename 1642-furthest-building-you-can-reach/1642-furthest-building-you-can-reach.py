class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        res = 0
        total = 0
        for i in range(0, len(heights) - 1):
            if heights[i] < heights[i + 1]:
                heapq.heappush(pq, heights[i] - heights[i + 1])
                total += heights[i + 1] - heights[i]
                while ladders > 0 and total > bricks:
                    ladders -= 1
                    total += heapq.heappop(pq)
                if total <= bricks:
                    res += 1
                else:
                    return res
            else:
                res += 1
        return res