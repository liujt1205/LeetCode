class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.isEnd = True
                    
        res = ""
        def has_all_prefix(word, root):
            cur = root
            for char in word:
                if char not in cur.children or not cur.children[char].isEnd:
                    return False
                cur = cur.children[char]
            return True
            
        for word in words:
            if has_all_prefix(word, root) and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word
                
        return res
                
        
        
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}