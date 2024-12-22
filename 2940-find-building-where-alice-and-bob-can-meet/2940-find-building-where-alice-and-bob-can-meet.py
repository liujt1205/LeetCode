class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        memo = [[] for _ in heights]
        for index, query in enumerate(queries):
            a, b = query
            if a < b and heights[a] < heights[b]:
                res[index] = b
            elif a > b and heights[a] > heights[b]:
                res[index] = a
            elif a == b:
                res[index] = a
            else:
                memo[max(a, b)].append((max(heights[a], heights[b]), index))
           
        pq = []
        for index, height in enumerate(heights):
            while pq and pq[0][0] < height:
                _, cur_index = heapq.heappop(pq)
                res[cur_index] = index
                
            for height, i in memo[index]:
                heapq.heappush(pq, (height, i))
                
        return res