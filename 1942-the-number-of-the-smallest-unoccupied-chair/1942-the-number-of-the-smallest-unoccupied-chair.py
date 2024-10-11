class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = sorted([(arrival, leave, index) for index, (arrival, leave) in enumerate(times)])
        
        totalChair = 0
        chairs = []
        current = []
        for time in times:
            arrival, leave, index = time
            while current and current[0][0] <= arrival:
                _, chairIndex = heapq.heappop(current)
                heapq.heappush(chairs, chairIndex)
                
            if chairs:
                cur_chair = heapq.heappop(chairs)
            else:
                cur_chair = totalChair
                totalChair += 1
                
            heapq.heappush(current, (leave, cur_chair))
            if index == targetFriend:
                return cur_chair
            
        return 0