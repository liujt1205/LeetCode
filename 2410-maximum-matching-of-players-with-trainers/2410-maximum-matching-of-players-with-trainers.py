class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        index = 0
        res = 0
        for player in players:
            while index < len(trainers) and trainers[index] < player:
                index += 1
            if index >= len(trainers):
                break
            index += 1
            res += 1
        
        return res