class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                n = board[r][c]

                if n == ".":
                    continue

                row_key = (r, n)
                col_key = (c, n)
                box_key = (r // 3, c // 3, n)

                if row_key in rows or col_key in cols or box_key in boxes:
                    return False

                rows.add(row_key)
                cols.add(col_key)
                boxes.add(box_key)

        return True