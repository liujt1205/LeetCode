class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for char in path:
            if char == '/':
                if cur == "" or cur == ".":
                    cur = ""
                elif cur == "..":
                    if len(stack) != 0:
                        stack.pop()
                    cur = ""
                else:
                    stack.append(cur)
                    cur = ""
            else:
                cur = cur + char
        
        if cur == ".." and len(stack) != 0:
            stack.pop()
        elif cur != "." and cur != "" and cur != "..":
            stack.append(cur)
            
        res = ""
        if len(stack) == 0:
            return "/"
        else:
            while len(stack) != 0:
                res = "/" + stack.pop() + res
                
        return res