class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToInt(stringTime):
            time = stringTime.split(":")
            intTime = int(time[0]) * 60 + int(time[1])
            return intTime
        
        times = []
        for time in timePoints:
            times.append(convertToInt(time))
            
        times.sort()
        
        res = 24 * 60 + 1
        for i in range(1, len(timePoints)):
            res = min(res, times[i] - times[i - 1])
            
        res = min(res, times[0] + 24 * 60 - times[-1])
        return res