class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        pq = []
        res = 0
        for i in range(len(nums)):
            if nums[i] == maximum:
                heapq.heappush(pq, i)
                if len(pq) > k:
                    heapq.heappop(pq)
            if len(pq) == k:
                res += pq[0] + 1
        return res