class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not cur.children[ord(char) - ord('a')]:
                cur.children[ord(char) - ord('a')] = TrieNode()
            cur = cur.children[ord(char) - ord('a')]
            cur.count += 1
        cur.end += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for char in word:
            if not cur.children[ord(char) - ord('a')]:
                return 0
            cur = cur.children[ord(char) - ord('a')]
        return cur.end

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if not cur.children[ord(char) - ord('a')]:
                return 0
            cur = cur.children[ord(char) - ord('a')]
        return cur.count

    def erase(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children[ord(char) - ord('a')]
            cur.count -= 1
        cur.end -= 1
                

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0
        self.end = 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)