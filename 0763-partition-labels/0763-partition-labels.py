class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexes = [[-1, -1] for _ in range(26)]
        for i in range(len(s)):
            curIndex = ord(s[i]) - ord('a')
            if indexes[curIndex][0] == -1:
                indexes[curIndex][0] = i
            indexes[curIndex][1] = i

        pq = []
        for i in range(26):
            if indexes[i][0] != -1:
                pq.append((indexes[i][0], indexes[i][1]))

        heapq.heapify(pq)
        start = pq[0][0]
        end = pq[0][1]
        res = []
        while pq:
            curStart, curEnd = heapq.heappop(pq)
            if curStart < start:
                continue
            if curStart > end:
                res.append(end + 1 - start)
                start = curStart
                end = curEnd
            else:
                end = max(end, curEnd)

        res.append(end + 1 - start)

        return res
