class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        for i in range(len(currentState) - 1):
            if currentState[i] == '+' and currentState[i + 1] == '+':
                if 0 < i < len(currentState) - 2:
                    res.append(currentState[:i] + "--" + currentState[i + 2:])
                elif i == 0:
                    res.append("--" + currentState[2:])
                elif i == len(currentState) - 2:
                    res.append(currentState[:i] + "--")
        return res