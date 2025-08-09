class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = deque()
        if x > y:
            first = 'a'
            second = 'b'
            large = x
            small = y
        else:
            first = 'b'
            second = 'a'
            large = y
            small = x

        res = 0
        for char in s:
            if char in [first, second]:
                if stack and char == second and stack[-1] == first:
                    stack.pop()
                    res += large
                else:
                    stack.append(char)
            else:
                while stack and stack[0] == second and stack[-1] == first:
                    stack.popleft()
                    stack.pop()
                    res += small
                stack = deque()

        while stack and stack[0] == second and stack[-1] == first:
            stack.popleft()
            stack.pop()
            res += small

        return res

        