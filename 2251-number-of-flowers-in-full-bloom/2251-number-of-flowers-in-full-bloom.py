class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = []
        end = []
        
        for a, b in flowers:
            start.append(a)
            end.append(b + 1)
            
        start.sort()
        end.sort()
        res = []
        
        for p in people:
            i = bisect_right(start, p)
            j = bisect_right(end, p)
            res.append(i - j)
            
        return res