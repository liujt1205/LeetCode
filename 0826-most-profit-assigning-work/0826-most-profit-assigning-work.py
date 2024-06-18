class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        sortJobs = sorted(zip(difficulty, profit))
        jobIndex = 0
        res = 0
        curMax = 0
        for cap in worker:
            while jobIndex < len(sortJobs) and sortJobs[jobIndex][0] <= cap:
                curMax = max(curMax, sortJobs[jobIndex][1])
                jobIndex += 1
            res += curMax
        return res
                