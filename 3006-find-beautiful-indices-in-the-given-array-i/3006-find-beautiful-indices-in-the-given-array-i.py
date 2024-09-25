class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        found_a = []
        found_b = []
        start = 0
        while start < len(s):
            start = s.find(a, start)
            if start != -1:
                found_a.append(start)
                start += 1
            else:
                break
                
        start = 0        
        while start < len(s):
            start = s.find(b, start)
            if start != -1:
                found_b.append(start)
                start += 1
            else:
                break
                
        res = []
        start = 0
        for i in range(len(found_a)):
            while start < len(found_b) and found_b[start] <= found_a[i] and abs(found_a[i] - found_b[start]) > k:
                start += 1
            if start >= len(found_b):
                break
            if found_b[start] > found_a[i] and abs(found_a[i] - found_b[start]) > k:
                continue
            else:
                res.append(found_a[i])
                    
        return res