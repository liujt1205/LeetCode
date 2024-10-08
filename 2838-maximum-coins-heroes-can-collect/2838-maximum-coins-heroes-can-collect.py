class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        sortedMonsters = sorted(list(zip(monsters, coins)), key=lambda x:x[0])
        newMonsters, newCoins = zip(*sortedMonsters)
        newMonsters = list(newMonsters)
        newCoins = list(newCoins)
        prev = 0
        for i in range(len(monsters)):
            newCoins[i] += prev
            prev = newCoins[i]
            
        res = [0] * len(heroes)
        
        for i in range(len(heroes)):
            index = bisect_right(newMonsters, heroes[i]) - 1
            if index >= 0:
                res[i] = newCoins[index]
            else:
                res[i] = 0
            
        return res