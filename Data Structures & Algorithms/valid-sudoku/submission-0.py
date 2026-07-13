class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # [["1","2",".",".","3",".",".",".","."],
        #  ["4",".",".","5",".",".",".",".","."],
        #  [".","9","8",".",".",".",".",".","3"],
        #  ["5",".",".",".","6",".",".",".","4"],
        #  [".",".",".","8",".","3",".",".","5"],
        #  ["7",".",".",".","2",".",".",".","6"],
        #  [".",".",".",".",".",".","2",".","."],
        #  [".",".",".","4","1","9",".",".","8"],
        #  [".",".",".",".","8",".",".","7","9"]]

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                    
                box = (r // 3, c // 3)

                if box not in boxes:
                    boxes[box] = set()

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True 
        