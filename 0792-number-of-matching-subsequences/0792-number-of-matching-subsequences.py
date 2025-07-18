class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)

        for word in words:
            it = iter(word)
            first_char = next(it, None)
            if first_char:
                waiting[first_char].append(it)

        count = 0
        for ch in s:
            # All iterators waiting on this character
            old_waiting = waiting[ch]
            waiting[ch] = []

            for it in old_waiting:
                nxt = next(it, None)
                if nxt:
                    waiting[nxt].append(it)
                else:
                    count += 1

        return count