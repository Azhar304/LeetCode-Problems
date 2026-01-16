class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = numRows
        values = [[" " for _ in range(len(s))] for _ in range(rows)]

        r = 0
        direction = 1
        c = 0

        for ch in s:
            values[r][c] = ch

            if r == 0:
                direction = 1
            elif r == rows - 1:
                direction = -1

            r += direction
            c += 1

        result = []
        for row in values:
            for ch in row:
                if ch != " ":
                    result.append(ch)

        return "".join(result)
