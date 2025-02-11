class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if len(part) > len(s):
            return s
        source = part + '#' + s
        find_part = [0] * len(source)
        for i in range(1, len(source)):
            prev = find_part[i - 1]
            if prev == len(part):
                move_left = len(part)
                index = i - 1
                while move_left:
                    index -= 1
                    move_left -= 1
                    if find_part[index] == len(part):
                        move_left += len(part)
                prev = find_part[index]
            while prev and source[i] != source[prev]:
                prev = find_part[prev - 1]

            find_part[i] = prev + (1 if source[i] == source[prev] else 0)

        print(find_part)

        res = []
        for i in range(len(part) + 1, len(source)):
            res.append(source[i])
            if find_part[i] == len(part):
                for _ in range(len(part)):
                    res.pop()

        return ''.join(res)