class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        sum_ratio = 0
        n = len(classes)
        pq = []
        for pas, tot in classes:
            cur_ratio = pas / tot
            sum_ratio += cur_ratio
            if cur_ratio != 1:
                change = (pas + 1) / (tot + 1) - cur_ratio
                pq.append((-change, pas + 1, tot + 1))
                
        heapq.heapify(pq)
        while pq and extraStudents > 0:
            change, pas, tot = heapq.heappop(pq)
            sum_ratio -= change
            extraStudents -= 1
            new_change = (pas + 1) / (tot + 1) - pas / tot
            heapq.heappush(pq, (-new_change, pas + 1, tot + 1))
            
        return sum_ratio / n
            