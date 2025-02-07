class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        count = 0
        res = []
        balls = defaultdict(int)
        for x, y in queries:
            if balls[x] != 0:
                colors[balls[x]] -= 1
                if colors[balls[x]] == 0:
                    count -= 1

            balls[x] = y
            colors[y] += 1
            if colors[y] == 1:
                count += 1
            
            res.append(count)

        return res