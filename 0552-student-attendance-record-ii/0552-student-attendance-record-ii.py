class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 1000000007
        A = 1
        L = [1, 0]
        P = [1, 0]
        LL = [0, 0]
        while n > 1:
            tempA, tempL, tempP, tempLL = 0, [0, 0], [0, 0], [0, 0]
            tempA = (L[0] + P[0] + LL[0]) % mod
            tempL[0] = P[0] % mod
            tempL[1] = (A + P[1]) % mod
            tempLL[0] = L[0] % mod
            tempLL[1] = L[1] % mod
            tempP[0] = (L[0] + LL[0] + P[0]) % mod
            tempP[1] = (L[1] + LL[1] + A + P[1]) % mod
            n -= 1
            A, L, P, LL = tempA, tempL, tempP, tempLL
            
        return (A + L[0] + L[1] + P[0] + P[1] + LL[0] + LL[1]) % mod