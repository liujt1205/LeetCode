class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        def fill(res, used, index, n):
            if index == len(res):
                return True
            
            if res[index] != 0:
                return fill(res, used, index + 1, n)

            for i in range(n, 0, -1):
                if used[i]:
                    continue
                
                used[i] = True
                res[index] = i
                if i == 1:
                    if fill(res, used, index + 1, n):
                        return True
                elif index + i < len(res) and res[index + i] == 0:
                    res[index + i] = i
                    if fill(res, used, index + 1, n):
                        return True
                    res[index + i] = 0
                
                res[index] = 0
                used[i] = False

            return False

        fill(res, used, 0, n)
        return res