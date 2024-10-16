"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        memo = defaultdict(int)
        for employee in schedule:
            for time in employee:
                memo[time.start] += 1
                memo[time.end] -= 1
                
        res = []
        started = None
        count = 0
        for i in sorted(memo.keys()):
            count += memo[i]
            if count == 0 and not started:
                started = i
            elif count != 0 and started:
                res.append(Interval(started, i))
                started = None
                
        return res