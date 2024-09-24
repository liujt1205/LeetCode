class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = [None] * 10
                
        class Trie:
            def __init__(self):
                self.root = TrieNode()
                
            def insert(self, num):
                cur = self.root
                str_num = str(num)
                for str_digit in str_num:
                    digit = int(str_digit)
                    if not cur.children[digit]:
                        cur.children[digit] = TrieNode()
                    cur = cur.children[digit]
            
            def find_longest(self, num):
                cur = self.root
                str_num = str(num)
                res = 0
                for str_digit in str_num:
                    digit = int(str_digit)
                    if cur.children[digit]:
                        res += 1
                        cur = cur.children[digit]
                    else:
                        break
                return res
            
        trie = Trie()
        for num in arr1:
            trie.insert(num)

        res = 0
        for num in arr2:
            longest = trie.find_longest(num)
            res = max(res, longest)

        return res