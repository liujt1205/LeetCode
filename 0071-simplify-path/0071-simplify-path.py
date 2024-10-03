class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for char in path.split('/'):
            if char == '.' or not char:
                continue
            elif char == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
                
        return '/' + '/'.join(stack)