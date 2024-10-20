class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == ')':
                has_true = False
                has_false = False
                while stack[-1] not in "!&|":
                    cur = stack.pop()
                    if cur == 't':
                        has_true = True
                    elif cur == 'f':
                        has_false = True
                operator = stack.pop()
                if operator == '!':
                    stack.append('t' if has_false else 'f')
                elif operator == '&':
                    stack.append('f' if has_false else 't')
                elif operator == '|':
                    stack.append('t' if has_true else 'f')
            elif char in 'tf!&|':
                stack.append(char)
        
        return stack[-1] == 't'