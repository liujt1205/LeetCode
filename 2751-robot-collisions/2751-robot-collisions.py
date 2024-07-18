class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        res = []
        stack = deque()
        indices.sort(key=lambda x: positions[x])
        for cur in indices:
            if directions[cur] == "R":
                stack.append(cur)
            else:
                while stack and healths[cur] > 0:
                    top = stack.pop()
                    if healths[top] > healths[cur]:
                        healths[top] -= 1
                        healths[cur] = 0
                        stack.append(top)
                    elif healths[top] < healths[cur]:
                        healths[cur] -= 1
                        healths[top] = 0
                    else:
                        healths[cur] = 0
                        healths[top] = 0
        for index in range(n):
            if healths[index] > 0:
                res.append(healths[index])
        return res