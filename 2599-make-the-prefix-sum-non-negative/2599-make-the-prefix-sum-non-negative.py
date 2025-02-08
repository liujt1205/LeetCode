class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        res = 0
        pq = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if num < 0:
                heapq.heappush(pq, num)

            while prefix_sum < 0:
                res += 1
                prefix_sum -= heapq.heappop(pq)

        return res