class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
            
        pq = [(-ord(char), cnt) for char, cnt in counts.items()]
        heapq.heapify(pq)
            
        res = []
        while pq:
            char_in, cnt = heapq.heappop(pq)
            char = chr(-char_in)
            use = min(repeatLimit, cnt)
            res.append(char * use)
            
            if cnt > use and pq:
                next_char_in, next_cnt = heapq.heappop(pq)
                res.append(chr(-next_char_in))
                if next_cnt > 1:
                    heapq.heappush(pq, (next_char_in, next_cnt - 1))
                    
                heapq.heappush(pq, (char_in, cnt - use))
                
        return "".join(res)
                
                            