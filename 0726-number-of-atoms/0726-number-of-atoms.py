class Solution:
    def countOfAtoms(self, formula: str) -> str:
        curMulti = 1
        stack = [1]
        finalMap = defaultdict(int)
        curAtom = ""
        curCount = ""
        index = len(formula) - 1
        while index >= 0:
            if formula[index].isdigit():
                curCount = formula[index] + curCount
            elif formula[index].islower():
                curAtom = formula[index] + curAtom
            elif formula[index].isupper():
                curAtom = formula[index] + curAtom
                if curCount:
                    finalMap[curAtom] += curMulti * int(curCount)
                else:
                    finalMap[curAtom] += curMulti
                curAtom = ""
                curCount = ""
            elif formula[index] == ")":
                multi = int(curCount) if curCount else 1
                stack.append(multi)
                curMulti *= multi
                curCount = ""
            elif formula[index] == "(":
                curMulti //= stack.pop()
            index -= 1
        finalMap = dict(sorted(finalMap.items()))
        res = ""
        for atom in finalMap:
            res += atom
            if finalMap[atom] > 1:
                res += str(finalMap[atom])
        return res
                
            