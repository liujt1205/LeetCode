class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occ = Counter(count.values())
        for i, cnt in occ.items():
            if cnt > 1:
                return False
        return True