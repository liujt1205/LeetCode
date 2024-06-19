class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        def check(x, bloomDay, m, k):
            count = 0
            bouquet = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= x:
                    count += 1
                    if count >= k:
                        bouquet += 1
                        count -= k
                    if bouquet >= m:
                        return True
                else:
                    count = 0
            return False
        
        start, end = min(bloomDay), max(bloomDay)
        while start < end:
            mid = start + (end - start) // 2
            if check(mid, bloomDay, m, k):
                end = mid
            else:
                start = mid + 1
        return start