class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        res = []
        for word in words:
            res.append(trie.getScore(word))
            
        return res
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for char in word:
            index = ord(char) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.score += 1
        
    def getScore(self, word):
        cur = self.root
        res = 0
        for char in word:
            index = ord(char) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            res += cur.score
        return res
        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.score = 0