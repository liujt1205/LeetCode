class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res = 0
        prev = 0
        meetings.sort()
        for start, end in meetings:
            if start > prev:
                res += start - prev - 1
                prev = end
            elif end > prev:
                prev = end

        if days > prev:
            res += days - prev

        return res