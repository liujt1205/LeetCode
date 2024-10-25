class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        for path in folder:
            path_list = list(filter(None, path.split('/')))
            if not path_list:
                continue
            cur = root
            for p in path_list:
                if p not in cur.children:
                    cur.children[p] = TrieNode()
                cur = cur.children[p]
            cur.isEnd = True
            
        res = []
        def helper(node, path):
            if node.isEnd:
                res.append(path)
                return
            for child in node.children:
                newPath = path + "/" + child
                helper(node.children[child], newPath)
                
        helper(root, "")
        return res
            
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False