class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = 1, (position[-1] - position[0] + 1) // (m - 1) + 1
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
                low = mid + 1
            else:
                high = mid - 1
        return low - 1