class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        proj = []
        for i in range(len(difficulty)):
            proj.append((-profit[i], difficulty[i]))
        heapq.heapify(proj)
        res = 0
        index = len(worker) - 1
        while proj and index >= 0:
            cur = heapq.heappop(proj)
            curProf, curDiff = -cur[0], cur[1]
            while index >= 0 and worker[index] >= curDiff:
                res += curProf
                index -= 1
        return res