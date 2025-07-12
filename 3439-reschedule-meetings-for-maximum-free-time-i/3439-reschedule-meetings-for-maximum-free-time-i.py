class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free = []
        prev = 0
        for i in range(len(startTime)):
            free.append(startTime[i] - prev)
            prev = endTime[i]
            if prev >= eventTime:
                prev = eventTime
                break

        free.append(eventTime - prev)

        left = 0
        cur = 0
        if k >= len(free) - 1:
            res = sum(free)

        for i in range(k + 1):
            cur += free[i]

        res = cur
        for i in range(k + 1, len(free)):
            cur += free[i]
            cur -= free[left]
            left += 1
            res = max(res, cur)

        return res