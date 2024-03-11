class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orders = [27] * 26
        for i in range(len(order)):
            orders[ord(order[i]) - ord('a')] = i
        def customSort(char):
            return orders[ord(char) - ord('a')]
        sortedS = ''.join(sorted(s, key=customSort))
        return sortedS