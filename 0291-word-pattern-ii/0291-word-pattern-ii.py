class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        memo = [""] * 26
        words = set()
        
        def check(s_index, p_index):
            if p_index == len(pattern):
                return s_index == len(s)
            cur = pattern[p_index]
            if memo[ord(cur) - ord('a')]:
                word = memo[ord(cur) - ord('a')]
                if s[s_index : s_index + len(word)] != word:
                    return False
                return check(s_index + len(word), p_index + 1)
            spots = 0
            for i in range(p_index + 1, len(pattern)):
                if memo[ord(pattern[i]) - ord('a')]:
                    spots += len(memo[ord(pattern[i]) - ord('a')])
                else:
                    spots += 1
            for j in range(s_index + 1, len(s) - spots + 1):
                new_word = s[s_index: j]
                if new_word in words:
                    continue
                memo[ord(cur) - ord('a')] = new_word
                words.add(new_word)
                if check(j, p_index + 1):
                    return True
                memo[ord(cur) - ord('a')] = ""
                words.remove(new_word)
            return False
        return check(0, 0)