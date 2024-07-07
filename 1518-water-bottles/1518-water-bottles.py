class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        emt = numBottles
        while emt >= numExchange:
            newBottles = emt // numExchange
            emt -= newBottles * numExchange
            res += newBottles
            emt += newBottles
        return res
        