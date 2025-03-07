class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def getPrime(right):
            res = [True] * (right + 1)
            res[0] = res[1] = False
            for num in range(2, int(right ** 0.5) + 1):
                if res[num]:
                    for multiple in range(num * num, right + 1, num):
                        res[multiple] = False
            
            return res

        primes = getPrime(right)

        primesInRange = [num for num in range(left, right + 1) if primes[num]]
        if len(primesInRange) < 2:
            return -1, -1

        min_diff = float('inf')
        res = (-1, -1)
        for i in range(1, len(primesInRange)):
            diff = primesInRange[i] - primesInRange[i - 1]
            if diff < min_diff:
                res = primesInRange[i - 1], primesInRange[i]
                min_diff = diff

        return res