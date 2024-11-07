class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        curNum = 0
        for char in s:
            if char == ' ':
                continue
            elif char == '(':
                stack.append('(')
            elif char == ')':
                if stack and stack[-1] == '-':
                    stack.pop()
                    curNum *= -1
                while stack[-1] != '(':
                    curNum += stack.pop()
                stack.pop()
                if stack and stack[-1] == '-':
                    stack.pop()
                    curNum *= -1
                stack.append(curNum)
                curNum = 0
            elif char == '+':
                if stack and stack[-1] == '-':
                    stack.pop()
                    curNum *= -1
                stack.append(curNum)
                curNum = 0
            elif char == '-':
                if stack and stack[-1] == '-':
                    stack.pop()
                    curNum *= -1
                stack.append(curNum)
                stack.append(char)
                curNum = 0
            else:
                curNum = curNum * 10 + int(char)
                
        if stack and stack[-1] == '-':
            stack.pop()
            curNum *= -1
        while stack:
            curNum += stack.pop()
            
        return curNum
                    