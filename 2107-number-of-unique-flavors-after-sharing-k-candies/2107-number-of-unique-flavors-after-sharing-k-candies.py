class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        count = defaultdict(int)
        diff = 0
        for candy in candies:
            count[candy] += 1
            if count[candy] == 1:
                diff += 1
         
        for i in range(k):
            count[candies[i]] -= 1
            if count[candies[i]] == 0:
                diff -= 1
              
        res = diff
        for i in range(k, len(candies)):
            count[candies[i]] -= 1
            if count[candies[i]] == 0:
                diff -= 1
            count[candies[i - k]] += 1
            if count[candies[i - k]] == 1:
                diff += 1
            res = max(res, diff)
            
        return res