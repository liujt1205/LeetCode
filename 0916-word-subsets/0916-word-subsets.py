class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        minCount = [0] * 26
        def count(string):
            res = [0] * 26
            for char in string:
                res[ord(char) - ord('a')] += 1
            return res

        for word in words2:
            counts = count(word)
            for i in range(26):
                minCount[i] = max(minCount[i], counts[i])

        res = []
        for word in words1:
            counts = count(word)
            valid = True
            for i in range(26):
                if counts[i] < minCount[i]:
                    valid = False
                    break
            if valid:
                res.append(word)

        return res