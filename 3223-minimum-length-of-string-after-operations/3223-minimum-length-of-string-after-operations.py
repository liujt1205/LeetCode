class Solution:
    def minimumLength(self, s: str) -> int:
        counts = Counter(s)
        res = 0
        for char, count in counts.items():
            if count > 2:
                res += 2 - count % 2
            else:
                res += count
        
        return res