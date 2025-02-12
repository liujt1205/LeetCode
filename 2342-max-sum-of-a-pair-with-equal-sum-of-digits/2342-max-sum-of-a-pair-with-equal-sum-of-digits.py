class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = defaultdict(list)
        def calSum(num):
            res = 0
            while num:
                res += num % 10
                num //= 10

            return res

        sums_seen = set()
        for num in nums:
            cur_sum = calSum(num)
            sums_seen.add(cur_sum)
            heapq.heappush(sums[cur_sum], num)
            if len(sums[cur_sum]) > 2:
                heapq.heappop(sums[cur_sum])

        sums_seen = sorted(list(sums_seen))
        res = -1
        for sum_seen in sums_seen:
            if len(sums[sum_seen]) == 2:
                res = max(res, sum(sums[sum_seen]))

        return res