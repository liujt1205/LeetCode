class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if not stack or num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and abs(num) > abs(stack[-1]):
                    stack.pop()
                if stack and stack[-1] + num == 0:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(num)
        
        return stack