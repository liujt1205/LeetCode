class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replaceMap = defaultdict(str)
        for key, value in replacements:
            replaceMap[key] = value

        def parse(s):
            res = []
            i = 0
            while i < len(s):
                if s[i] == '%':
                    if '%' in replaceMap[s[i + 1]]:
                        replaceMap[s[i + 1]] = parse(replaceMap[s[i + 1]])
                    res.append(replaceMap[s[i + 1]])
                    i += 3
                else:
                    res.append(s[i])
                    i += 1

            return ''.join(res)
        
        return parse(text)