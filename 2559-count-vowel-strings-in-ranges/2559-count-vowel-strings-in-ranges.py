class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            prefix[i + 1] = prefix[i]
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                prefix[i + 1] += 1
        
        res = []
        for start, end in queries:
            res.append(prefix[end + 1] - prefix[start])

        return res