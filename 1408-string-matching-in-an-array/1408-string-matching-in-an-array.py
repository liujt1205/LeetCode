class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        root = TrieNode()
        def insert(root, word):
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
                cur.count += 1

        def check(root, word):
            cur = root
            for char in word:
                if char not in cur.children:
                    return False
                cur = cur.children[char]
            return cur.count > 1

        res = []
        for word in words:
            for i in range(len(word)):
                insert(root, word[i:])

        for word in words:
            if check(root, word) == True:
                res.append(word)

        return res

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0