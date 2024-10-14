class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        pq = []
        for i in range(len(keyName)):
            name = keyName[i]
            time = int(keyTime[i][:2]) * 60 + int(keyTime[i][3:])
            pq.append((time, name))
        
        pq.sort()
        count = {}
        res = set()
        left = 0
        for right in range(len(pq)):
            curTime, curName = pq[right]
            while left <= right and pq[left][0] + 60 < curTime:
                count[pq[left][1]] -= 1
                left += 1
            
            if curName not in count:
                count[curName] = 0
            count[curName] += 1
            
            if count[curName] >= 3:
                res.add(curName)

        return sorted(list(res))