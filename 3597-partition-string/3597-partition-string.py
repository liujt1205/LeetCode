class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        segment = ""
        for char in s:
            segment += char
            if segment not in seen:
                seen.add(segment)
                res.append(segment)
                segment = ""

        return res
            
