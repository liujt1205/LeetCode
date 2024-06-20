class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = 1, position[-1] // (m - 1)
        res = 0
        while low <= high:
            mid = (low + high) // 2
            count = 1
            pre = position[0]
            for pos in position:
                if pos - pre >= mid:
                    pre = pos
                    count += 1
                if count == m:
                    break
            if count == m:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res