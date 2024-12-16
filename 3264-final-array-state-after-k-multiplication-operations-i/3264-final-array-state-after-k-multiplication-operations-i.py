class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for i, num in enumerate(nums):
            pq.append((num, i))
            
        heapq.heapify(pq)
        
        while k > 0:
            num, i = heapq.heappop(pq)
            num = num * multiplier
            nums[i] = num
            k -= 1
            heapq.heappush(pq, (num, i))
            
        return nums