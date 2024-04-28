class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        index = defaultdict(set)
        memo = [0] * n
        def dist(preIndex, curIndex):
            distance = abs(preIndex - curIndex)
            return min(distance, abs(distance-n))
        
        for i in range(n):
            index[ring[i]].add(i)
            
        pq = [(0, 0, 0)]
        seen = set()
        while pq:
            curSteps, curIndex, keyIndex = heapq.heappop(pq)
            if keyIndex == m:
                break
            if (curIndex, keyIndex) in seen:
                continue
            seen.add((curIndex, keyIndex))
            for nextIndex in index[key[keyIndex]]:
                heapq.heappush(pq, ((curSteps + dist(curIndex, nextIndex)), nextIndex, keyIndex + 1))
        return curSteps + m
        
            