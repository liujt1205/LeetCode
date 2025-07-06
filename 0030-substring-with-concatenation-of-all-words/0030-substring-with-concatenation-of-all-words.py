class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words[0])
        k = len(words)
        res = []
        if n < m * k:
            return res

        counts = Counter(words)

        def check(left):
            found = defaultdict(int)
            used = 0
            extra = False

            for right in range(left, n, m):
                if right + m > n:
                    break
                
                sub = s[right: right + m]
                if sub not in counts:
                    found = defaultdict(int)
                    used = 0
                    extra = False
                    left = right + m
                else:
                    while right - left == m * k or extra:
                        left_word = s[left: left + m]
                        left += m
                        found[left_word] -= 1
                        if found[left_word] == counts[left_word]:
                            extra = False
                        else:
                            used -= 1
                    found[sub] += 1
                    if found[sub] <= counts[sub]:
                        used += 1
                    else:
                        extra = True
                    
                    if used == k and not extra:
                        res.append(left)

        for i in range(m):
            check(i)

        return res