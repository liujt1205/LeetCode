class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        memo = deque()
        for i in range(n - 1, -1, -1):
            count = 0
            while memo and memo[0] <= heights[i]:
                memo.popleft()
                count += 1
            if memo:
                count += 1
            res[i] = count
            memo.appendleft(heights[i])

        return res
