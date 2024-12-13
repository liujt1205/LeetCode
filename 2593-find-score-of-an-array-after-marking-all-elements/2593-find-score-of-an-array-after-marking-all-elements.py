class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        pq = []
        for i, num in enumerate(nums):
            pq.append((num, i))
            
        heapq.heapify(pq)
        
        while pq:
            cur, index = heapq.heappop(pq)
            if nums[index] != 0:
                score += nums[index]
                nums[index] = 0
                if index > 0:
                    nums[index - 1] = 0
                if index < len(nums) - 1:
                    nums[index + 1] = 0
                    
        return score