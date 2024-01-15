class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        memo = {}
        for i in range(len(matches)):
            winner, loser = matches[i]
            if winner not in memo:
                memo[winner] = [0, 0]
            if loser not in memo:
                memo[loser] = [0, 0]
            memo[winner][0] += 1
            memo[loser][1] += 1
        res = [[], []]
        for player in memo.keys():
            if memo[player][1] == 0:
                res[0].append(player)
            elif memo[player][1] == 1:
                res[1].append(player)
        res[1].sort()
        res[0].sort()
        return res