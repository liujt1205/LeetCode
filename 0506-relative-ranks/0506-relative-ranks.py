class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pq = []
        n = len(score)
        for i in range(n):
            heapq.heappush(pq, (-score[i], i))
        place = 1
        res = [0] * n
        while pq:
            _, index = heapq.heappop(pq)
            if place > 3:
                res[index] = str(place)
            elif place == 1:
                res[index] = "Gold Medal"
            elif place == 2:
                res[index] = "Silver Medal"
            elif place == 3:
                res[index] = "Bronze Medal"
            place += 1
        return res