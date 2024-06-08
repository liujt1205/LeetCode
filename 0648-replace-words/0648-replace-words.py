class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode:
            def __init__(self):
                self.isEnd = False
                self.children = [None] * 26
        
        root = TrieNode()
        for word in dictionary:
            cur = root
            for char in word:
                if cur.children[ord(char) - ord('a')] is None:
                    cur.children[ord(char) - ord('a')] = TrieNode()
                cur = cur.children[ord(char) - ord('a')]
            cur.isEnd = True
        
        words = sentence.split(' ')
        res = []
        for word in words:
            cur = root
            found = False
            for i in range(len(word)):
                if cur.children[ord(word[i]) - ord('a')] is None:
                    res.append(word)
                    found = True
                    break
                cur = cur.children[ord(word[i]) - ord('a')]
                if cur.isEnd:
                    res.append(word[:i + 1])
                    found = True
                    break
            if not found:
                res.append(word)
        
        return " ".join(res)