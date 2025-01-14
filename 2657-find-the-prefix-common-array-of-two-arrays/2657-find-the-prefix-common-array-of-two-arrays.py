class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        seen = set()
        for i in range(n):
            if i > 0:
                res[i] += res[i - 1]
            if A[i] in seen:
                res[i] += 1
                seen.remove(A[i])
            else:
                seen.add(A[i])
            if B[i] in seen:
                res[i] += 1
                seen.remove(B[i])
            else:
                seen.add(B[i])

        return res