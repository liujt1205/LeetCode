class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        curMax = 0
        for i in range(len(items)):
            curMax = max(curMax, items[i][1])
            items[i][1] = curMax
            
        def find(items, q):
            left, right = 0, len(items) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if items[mid][0] <= q:
                    left = mid + 1
                else:
                    right = mid - 1
            return 0 if right < 0 else items[right][1]
        
        return [find(items, q) for q in queries]