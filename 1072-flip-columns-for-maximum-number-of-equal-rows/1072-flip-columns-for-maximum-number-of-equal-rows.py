class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_frequency = {}
        for current_row in matrix:
            row_pattern = "".join(
                "T" if num == current_row[0] else "F" for num in current_row
            )

            pattern_frequency[row_pattern] = (
                pattern_frequency.get(row_pattern, 0) + 1
            )

        return max(pattern_frequency.values(), default=0)