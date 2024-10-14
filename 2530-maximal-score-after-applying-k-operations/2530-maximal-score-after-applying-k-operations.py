class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        res = 0
        while k > 0:
            highest = heapq.heappop(maxHeap)
            res += - highest
            highest = -ceil(-highest / 3)
            heapq.heappush(maxHeap, highest)
            k -= 1
            
        return res