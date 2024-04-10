class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        res = len(tickets) * (target - 1) + k + 1
        for i in range(len(tickets)):
            ticket = tickets[i]
            if ticket < target and i < k:
                res -= target - ticket
            elif ticket < target - 1 and i > k:
                res -= target - 1 - ticket
        return res
        