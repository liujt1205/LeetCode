class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        memo = defaultdict(int)
        for start, end in firstList:
            memo[start] += 1
            memo[end + 0.5] -= 1
            
        for start, end in secondList:
            memo[start] += 1
            memo[end + 0.5] -= 1
            
        res = []
        count = 0
        start = -1
        for time in sorted(memo.keys()):
            count += memo[time]
            if count == 2:
                start = time
            elif start >= 0 and count < 2:
                res.append([start, int(time - 0.5)])
                start = -1
        
        return res