class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        total = [0] * (n + 1)
        mod = 1000000007
        for i in range(1, n + 1):
            total[i] = total[i - 1] + strength[i - 1]
        pre = [0] * (n + 2)
        for i in range(1, n + 2):
            pre[i] = pre[i - 1] + total[i - 1]
        # find index for the first smaller item on the right
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        # find index for the first smaller item on the left
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(n):
            leftLimit = left[i]
            rightLimit = right[i]
            leftCount = i - leftLimit
            rightCount = rightLimit - i
            neg = (pre[i + 1] - pre[i - leftCount + 1]) % mod
            pos = (pre[rightCount + i + 1] - pre[i + 1]) % mod
            res += strength[i] * (pos * leftCount - neg * rightCount)
            res %= mod
        return res
        