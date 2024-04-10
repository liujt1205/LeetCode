class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = [0] * len(deck)
        queue = deque()
        for i in range(len(deck)):
            queue.append(i)
        deck.sort()
        for card in deck:
            res[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return res