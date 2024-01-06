class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        memo = {}
        existing = set()
        for i in range(len(words)):
            cur = pattern[i]
            if memo.get(cur, '') == '':
                memo[cur] = words[i]
                if words[i] in existing:
                    return False
                else:
                    existing.add(words[i])
            elif memo.get(cur, '') != words[i]:
                return False
        return True