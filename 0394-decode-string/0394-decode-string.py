class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ""
        curNum = ""
        for char in s:
            if char.isdigit():
                if curString:
                    stack.append(curString)
                    curString = ""
                curNum = curNum + char
            elif char == '[':
                stack.append(curNum)
                curNum = ""
            elif char == ']':
                while stack and not stack[-1].isdigit():
                    curString = stack.pop() + curString
                num = stack.pop()
                newString = curString * int(num)
                curString = ""
                while stack and not stack[-1].isdigit():
                    newString = stack.pop() + newString
                stack.append(newString)
            else:
                curString = curString + char
                
        while stack and not stack[-1].isdigit():
            curString = stack.pop() + curString
        stack.append(curString)
                
        return stack.pop()