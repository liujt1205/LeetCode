class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        pos1 = 0
        pos2 = 0
        slots1.sort()
        slots2.sort()
        while pos1 < len(slots1) and pos2 < len(slots2):
            if slots1[pos1][0] >= slots2[pos2][1]:
                pos2 += 1
            elif slots2[pos2][0] >= slots1[pos1][1]:
                pos1 += 1
            else:
                start = max(slots1[pos1][0], slots2[pos2][0])
                end = min(slots1[pos1][1], slots2[pos2][1])
                if end - start >= duration:
                    return [start, start + duration]
                else:
                    if slots2[pos2][1] > slots1[pos1][1]:
                        pos1 += 1
                    else:
                        pos2 += 1
        return []