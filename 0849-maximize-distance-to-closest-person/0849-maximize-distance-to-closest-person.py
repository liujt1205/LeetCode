class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        count = 0
        i = 0
        while i < len(seats) and seats[i] == 0:
            count += 1
            i += 1
            
        res = count
        while i < len(seats):
            if seats[i] == 0:
                count += 1
            else:
                res = max(res, (count + 1) // 2)
                count = 0
            i += 1
            
        res = max(res, count)
        return res