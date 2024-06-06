class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for num in sorted(count):
            if count[num] < 0:
                return False
            elif count[num] > 0:
                for i in range(1, groupSize):
                    if count[num + i] < count[num]:
                        return False
                    else:
                        count[num + i] -= count[num]
        return True