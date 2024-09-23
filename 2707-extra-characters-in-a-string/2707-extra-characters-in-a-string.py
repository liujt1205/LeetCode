class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
            
        dp = [i for i in range(len(s) + 1)]
        dp[0] = 0
            
        for i in range(1, len(s) + 1):
            dp[i] = min(dp[i], dp[i - 1] + 1)
            trie.findWord(s, i - 1, dp)
        return dp[len(s)]
        
class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isEnd = False
            
    def __init__(self):
        self.root = Trie.TrieNode()
        
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie.TrieNode()
            cur = cur.children[char]
        cur.isEnd = True
        
    def findWord(self, s, start, dp):
        best = dp[start]
        found = 0
        cur = self.root
        while start + found < len(s) and s[start + found] in cur.children:
            cur = cur.children[s[start + found]]
            found += 1
            if cur.isEnd:
                dp[start + found] = min(best, dp[start + found])
            