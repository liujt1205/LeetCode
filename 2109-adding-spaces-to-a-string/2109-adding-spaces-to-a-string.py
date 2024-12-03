class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        index = 0
        space_index = 0
        while index < len(s):
            if space_index < len(spaces) and index == spaces[space_index]:
                res += " "
                space_index += 1
            res += s[index]
            index += 1
        
        return res