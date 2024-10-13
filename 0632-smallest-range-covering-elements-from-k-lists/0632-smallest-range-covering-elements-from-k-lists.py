class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        biggest = -float('inf')
        for i in range(len(nums)):
            biggest = max(biggest, nums[i][0])
            heapq.heappush(pq, (nums[i][0], i, 0))
          
        res = [None, None]
        gap = float('inf')
        while True:
            smallest, i, index = heapq.heappop(pq)
            if gap > biggest - smallest:
                gap = biggest - smallest
                res[0] = smallest
                res[1] = biggest
            if index == len(nums[i]) - 1:
                break
            biggest = max(biggest, nums[i][index + 1])
            heapq.heappush(pq, (nums[i][index + 1], i, index + 1))
            
        return res