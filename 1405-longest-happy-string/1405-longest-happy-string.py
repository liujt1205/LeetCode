class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        pq = []
        if a:
            heapq.heappush(pq, (-a, "a"))
        if b:
            heapq.heappush(pq, (-b, "b"))
        if c:
            heapq.heappush(pq, (-c, "c"))
            
        while pq:
            first, char = heapq.heappop(pq)
            if not pq:
                res += char * min(2, -first)
                return res
            elif first + 1 < pq[0][0]:
                second, nextChar = heapq.heappop(pq)
                res += char * 2 + nextChar
                heapq.heappush(pq, (first + 2, char))
                if second + 1 < 0:
                    heapq.heappush(pq, (second + 1, nextChar))
            else:
                second, nextChar = heapq.heappop(pq)
                res += char + nextChar
                if first + 1 < 0:
                    heapq.heappush(pq, (first + 1, char))
                if second + 1 < 0:
                    heapq.heappush(pq, (second + 1, nextChar))
            
        return res