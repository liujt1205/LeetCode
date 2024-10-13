class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        cumulate = parts = index = 0
        while 3 + len(str(parts)) * 2 < limit and cumulate + len(message) + (3 + len(str(parts))) * parts > limit * parts:
            parts += 1
            cumulate += len(str(parts))
        res = []
        if 3 + len(str(parts)) * 2 < limit:
            for i in range(1, parts + 1):
                length = limit - (len(str(i)) + 3 + len(str(parts)))
                res.append('%s<%s/%s>' % (message[index:index + length], i, parts))
                index += length
        return res