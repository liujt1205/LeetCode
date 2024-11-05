class Solution:
    def alienOrder(self, words: List[str]) -> str:
        child = [set() for _ in range(26)]
        degree = [0] * 26
        seen = set()
        def transform(index):
            word = []
            for char in words[index]:
                word.append(ord(char) - ord('a'))
            return word
            
        def findDiff(index):
            i = 0
            word1 = transform(index)
            word2 = transform(index + 1)
            seen.update(word1)
            seen.update(word2)
            while i < len(word1) and i < len(word2):
                if word1[i] != word2[i]:
                    if word2[i] not in child[word1[i]]:
                        child[word1[i]].add(word2[i])
                        degree[word2[i]] += 1
                    return True
                i += 1
            return i == len(word1)
        
        if len(words) == 1:
            return ''.join(list(set(words[0])))
        for i in range(len(words) - 1):
            if(not findDiff(i)):
                return ""
            
        queue = deque()
        for i in seen:
            if degree[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            cur = queue.popleft()
            res.append(chr(ord('a') + cur))
            for i in child[cur]:
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)
                    
        if len(res) != len(seen):
            return ""
        else:
            return ''.join(res)