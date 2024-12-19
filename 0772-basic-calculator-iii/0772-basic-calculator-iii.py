class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curNum = 0
        preOp = '+'
        def cal(curNum, preOp):
            nonlocal stack
            if preOp == '*':
                preNum = stack.pop()
                curNum *= preNum
            elif preOp == '-':
                curNum *= -1
            elif preOp == '/':
                preNum = stack.pop()
                add = 1 if preNum % curNum != 0 and preNum * curNum < 0 else 0
                curNum = preNum // curNum + add
                
            return curNum
            
        for char in s:
            if char.isdigit():
                curNum = curNum * 10 + int(char)
            elif char in '+-*/':
                curNum = cal(curNum, preOp)
                preOp = char
                stack.append(curNum)
                curNum = 0
            elif char == '(':
                stack.append(preOp)
                stack.append(char)
                preOp = '+'
                curNum = 0
            elif char == ')':
                curNum = cal(curNum, preOp)
                while stack and stack[-1] != '(':
                    curNum += stack.pop()
                stack.pop()
                if stack and stack[-1] in '+-*/':
                    preOp = stack.pop()
                    curNum = cal(curNum, preOp)
                preOp = '+'
            else:
                print("unexpected char: " + char)
                
        curNum = cal(curNum, preOp)
        while stack:
            curNum += stack.pop()
        stack.append(curNum)
            
        return stack[0]
                
                