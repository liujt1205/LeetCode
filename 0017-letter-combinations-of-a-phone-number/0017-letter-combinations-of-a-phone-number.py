class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit = 0
        if len(digits) == 0:
            return []
        res = [""]
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        while digit < len(digits):
            temp = []
            for string in res:
                for char in letters[digits[digit]]:
                    temp.append(string + char)
            res = temp
            digit += 1
        return res