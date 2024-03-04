class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        res = 0
        n = len(tokens)
        left = 0
        right = n - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                res = max(res, score)
                left += 1
            else:
                if score > 0:
                    power += tokens[right]
                    score -= 1
                    right -= 1
                else:
                    break
        return res