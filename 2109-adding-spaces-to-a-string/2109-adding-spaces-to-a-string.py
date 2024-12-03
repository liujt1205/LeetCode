class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        space_index = 0
        for index in range(len(s)):
            if space_index < len(spaces) and index == spaces[space_index]:
                res += " "
                space_index += 1
            res += s[index]
        
        return res