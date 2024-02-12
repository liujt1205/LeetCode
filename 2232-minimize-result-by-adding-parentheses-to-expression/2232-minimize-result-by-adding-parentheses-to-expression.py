class Solution:
    def minimizeResult(self, expression: str) -> str:
        curBest = float('inf')
        res = expression
        first, second = expression.split('+')
        m = len(first)
        n = len(second)
        for left in range(m):
            for right in range(n):
                a = int(first[:left]) if left != 0 else 1
                b = int(first[left:])
                c = int(second[:n - right])
                d = int(second[n - right:]) if right != 0 else 1
                cur = a * d * (b + c)
                if cur < curBest:
                    res = expression[:left] + "(" + expression[left:m + n + 1 - right] + ")" + expression[m + n + 1 - right:]
                    curBest = cur
        print(curBest)
        return res