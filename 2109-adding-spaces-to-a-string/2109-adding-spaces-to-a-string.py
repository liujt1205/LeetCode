class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        space_index = 0
        for index in range(len(s)):
            if space_index < len(spaces) and index == spaces[space_index]:
                res.append(" ")
                space_index += 1
            res.append(s[index])
        
        return "".join(res)