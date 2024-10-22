class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(string):
            res = [0] * len(string)
            for i in range(1, len(string)):
                cur = res[i - 1]
                while cur and string[i] != string[cur]:
                    cur = res[cur - 1]
                res[i] = cur + (string[i] == string[cur])
                
            return res
            
        indexes_a = kmp(a + "#" + s)
        indexes_b = kmp(b + "#" + s)

        found_a = [i - len(a) * 2 for i, v in enumerate(indexes_a) if v == len(a)]
        found_b = [i - len(b) * 2 for i, v in enumerate(indexes_b) if v == len(b)]
              
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