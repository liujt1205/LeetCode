class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        words.add(beginWord)
        neighbors = defaultdict(set)
        shortest = {}
        for word in wordList:
            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(ord('a') + j) + word[i + 1:]
                    if newWord != word and newWord in words and newWord not in neighbors[word]:
                        neighbors[word].add(newWord)
                        neighbors[newWord].add(word)
                        
        if endWord not in neighbors:
            return 0
        queue = deque([(beginWord, 0)])
                    
        while queue:
            curWord, step = queue.popleft()
            if curWord in shortest:
                continue
            if curWord == endWord:
                return step + 1
            shortest[curWord] = step + 1
            for neighbor in neighbors[curWord]:
                if neighbor not in shortest:
                    queue.append((neighbor, step + 1))
                    
        return 0
        