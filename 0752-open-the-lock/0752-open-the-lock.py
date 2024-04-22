class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set()
        deadendset = set(deadends)
        queue = deque()
        queue.append('0000')
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return step
                if cur not in deadendset and cur not in seen:
                    seen.add(cur)
                    for i in range(4):
                        goUp = list(cur)
                        goUp[i] = str((int(goUp[i]) + 1) % 10)
                        newCombo = "".join(goUp)
                        queue.append(newCombo)
                        goDown = list(cur)
                        goDown[i] = str((int(goDown[i]) + 9) % 10)
                        newCombo = "".join(goDown)
                        queue.append(newCombo)
            step += 1
        return -1
                
                