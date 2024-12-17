class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(string, sub):
            combined = sub + '#' + string
            target = [0] * len(combined)
            for i in range(1, len(combined)):
                cur = target[i - 1]
                while cur and combined[cur] != combined[i]:
                    cur = target[cur - 1]
                target[i] = cur + (combined[cur] == combined[i])
                
            res = []
            for i in range(len(target)):
                if target[i] == len(sub):
                    res.append(i - len(sub) * 2)
                    
            return res
        
        indexA = kmp(s, a)
        indexB = kmp(s, b)
        
        res = []
        index = 0
        for i in range(len(indexA)):
            while index < len(indexB) and indexB[index] + k < indexA[i]:
                index += 1
            
            if index < len(indexB) and indexB[index] <= k + indexA[i]:
                res.append(indexA[i])
                
        return res