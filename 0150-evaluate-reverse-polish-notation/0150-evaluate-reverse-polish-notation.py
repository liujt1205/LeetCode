class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                second = stack.pop()
                first = stack.pop()
                new = first + second
                stack.append(new)
            elif tokens[i] == '-':
                second = stack.pop()
                first = stack.pop()
                new = first - second
                stack.append(new)
            elif tokens[i] == '*':
                second = stack.pop()
                first = stack.pop()
                new = first * second
                stack.append(new)
            elif tokens[i] == '/':
                second = stack.pop()
                first = stack.pop()
                if second * first < 0:
                    new = - (abs(first) // abs(second))
                else:
                    new = first // second
                stack.append(new)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
                