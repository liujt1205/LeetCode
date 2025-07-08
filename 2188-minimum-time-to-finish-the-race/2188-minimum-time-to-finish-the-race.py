class Solution:
    def preprocess(self, tires: List[List[int]]) -> List[List[int]]:
        tires.sort()
        new_tires = []
        for t in tires:
            if not new_tires or new_tires[-1][1] > t[1]:
                new_tires.append(t)
        return new_tires

    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        tires = self.preprocess(tires)
        n = len(tires)

        max_laps = 20
        INF = float('inf')
        lap_time = [INF] * (max_laps + 1)

        for f, r in tires:
            time = 0
            current = f
            for i in range(1, max_laps + 1):
                time += current
                if time > 1e7:
                    break
                lap_time[i] = min(lap_time[i], time)
                current *= r

        dp = [INF] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            for l in range(1, min(i, max_laps) + 1):
                dp[i] = min(dp[i], dp[i - l] + lap_time[l] + (0 if i == l else changeTime))

        return dp[numLaps]