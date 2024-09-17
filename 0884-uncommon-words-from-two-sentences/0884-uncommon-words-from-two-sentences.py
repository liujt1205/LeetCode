class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        memo1 = {}
        memo2 = {}
        words1 = s1.split(" ")
        words2 = s2.split(" ")
        for word in words1:
            if word in memo1:
                memo1[word] += 1
            else:
                memo1[word] = 1
        
        for word in words2:
            if word in memo2:
                memo2[word] += 1
            else:
                memo2[word] = 1
                
        res = []
        for word in memo1:
            if memo1[word] == 1 and word not in memo2:
                res.append(word)
        
        for word in memo2:
            if memo2[word] == 1 and word not in memo1:
                res.append(word)
                
        return res