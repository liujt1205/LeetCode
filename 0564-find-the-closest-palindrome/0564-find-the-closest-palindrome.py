class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def buildPalindrome(half, even):
            res = half
            if not even:
                half //= 10
            while half > 0:
                res = res * 10 + half % 10
                half //= 10
            return res
        
        potential = []
        mid = len(n) // 2 - 1 if len(n) % 2 == 0 else len(n) // 2
        potential.append(buildPalindrome(int(n[:mid + 1]), len(n) % 2 == 0))
        potential.append(buildPalindrome(int(n[:mid + 1]) + 1, len(n) % 2 == 0))
        potential.append(buildPalindrome(int(n[:mid + 1]) - 1, len(n) % 2 == 0))
        potential.append(10 ** (len(n) - 1) - 1)
        potential.append(10 ** len(n) + 1)
        
        best = 0
        diff = float('inf')
        for num in potential:
            if num == int(n): 
                continue
            curDiff = abs(num - int(n))
            if curDiff < diff:
                diff = curDiff
                best = num
            elif curDiff == diff:
                best = min(best, num)
                
        return str(best)