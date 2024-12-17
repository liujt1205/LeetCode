class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(string):
            res = [0] * len(string)
            for i in range(1, len(string)):
                cur = res[i - 1]
                while cur and string[cur] != string[i]:
                    cur = res[cur - 1]
                res[i] = cur + (string[cur] == string[i])
            return res
        
        foundA = kmp(a + '#' + s)
        foundB = kmp(b + '#' + s)
        indexA = [i - 2 * len(a) for i in range(len(foundA)) if foundA[i] == len(a)]
        indexB = [i - 2 * len(b) for i in range(len(foundB)) if foundB[i] == len(b)]
        
        res = []
        index = 0
        for i in range(len(indexA)):
            while index < len(indexB) and indexB[index] + k < indexA[i]:
                index += 1
            
            if index < len(indexB) and indexB[index] <= k + indexA[i]:
                res.append(indexA[i])
                
        return res