class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def getDiff(line, sq):
            above = 0.0
            below = 0.0
            for x, y, l in sq:
                total = l * l
                if line <= y:
                    above += total
                elif line >= y + l:
                    below += total
                else:
                    abovePart = (y + l) - line
                    belowPart = line - y
                    above += l * abovePart
                    below += l * belowPart
            return above - below

        low = 0
        high = max([y + l for x, y, l in squares])

        diff = 1
        for _ in range(50):
            mid = (low + high) / 2.0
            curDiff = getDiff(mid, squares)
            if curDiff > 0:
                low = mid
            else:
                high = mid

        return mid