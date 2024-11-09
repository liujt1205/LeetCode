class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orders = [27] * 26
        for i in range(len(order)):
            orders[ord(order[i]) - ord('a')] = i
        
        sortedS = ''.join(sorted(s, key=lambda char: orders[ord(char) - ord('a')]))
        return sortedS