class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefix = TrieNode()
        suffix = TrieNode()
        res = 0
        for word in words:
            prefix_set = set()
            cur = prefix
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
                if cur.isEnd != False:
                    prefix_set.add((cur.isEnd, cur.count))
            cur.isEnd = word
            cur.count += 1

            suffix_set = set()
            cur = suffix
            for i in range(len(word) - 1, -1, -1):
                if word[i] not in cur.children:
                    cur.children[word[i]] = TrieNode()
                cur = cur.children[word[i]]
                if cur.isEnd != False:
                    suffix_set.add(cur.isEnd)
            cur.isEnd = word

            for p, count in prefix_set:
                if p in suffix_set:
                    res += count

        return res

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0