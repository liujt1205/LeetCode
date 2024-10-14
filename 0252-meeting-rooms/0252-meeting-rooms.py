class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev = -float('inf')
        for start, end in intervals:
            if start < prev:
                return False
            prev = end
            
        return True