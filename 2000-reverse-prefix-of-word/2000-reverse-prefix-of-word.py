class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        res = []
        index = 0
        while index < len(word):
            stack.append(word[index])
            if word[index] == ch:
                while stack:
                    res.append(stack.pop())
                index += 1
                while index < len(word):
                    res.append(word[index])
                    index += 1
                return ''.join(res)
            index += 1
        return word