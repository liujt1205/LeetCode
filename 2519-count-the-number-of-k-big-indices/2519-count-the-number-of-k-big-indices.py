class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        if n < 2* k:
            return 0
        memo = [False] * n
        small = []
        for i in range(n):
            if len(small) < k:
                heapq.heappush(small, -nums[i])
            else:
                if nums[i] + small[0] <= 0:
                    heapq.heappush(small, -nums[i])
                    heapq.heappop(small)
                else:
                    memo[i] = True
        small = []
        for i in range(n-1, -1, -1):
            if len(small) < k:
                heapq.heappush(small, -nums[i])
            else:
                if nums[i] + small[0] <= 0:
                    heapq.heappush(small, -nums[i])
                    heapq.heappop(small)
                else:
                    if memo[i] == True:
                        res += 1
        return res