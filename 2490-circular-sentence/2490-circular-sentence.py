class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        prev = words[-1][-1]
        for word in words:
            if word[0] != prev:
                return False
            else:
                prev = word[-1]

        return True