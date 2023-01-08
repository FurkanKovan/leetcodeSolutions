# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/valid-sudoku/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def isValidSudoku(self, board: List[List[str]]) -> bool:
        # (1) Create hashsets for each constraint, 1-no dups in each row, 2-no dups in each col, 3-no dups in each block
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        blocks = collections.defaultdict(set)

        # (2) Since the board is always 9 by 9, loop for each row until 9, then for each column until 9
        for r in range(9):
            for c in range(9):
                # Empty spots are represented with a dot, so skip
                if board[r][c] == '.':
                    continue
                # (3) If a encountered (row,col) element is already in one of the hashsets, there is a duplicate
                # To map the each block on board, divide it into 3 by 3 blocks -> ((0,0),(0,1),(0,2),...,(2,0),(2,1),(2,2))
                # Now each number can add it to its own block, which maps as
                # blocks[0,0] : board[0-2][0-2] | blocks[0,1] : board[0-2][3-5] | ... | blocks[2,2] : board[6-8][6-8]
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in blocks[(r//3, c//3)]): # int-divided by 3 to map to 3 by 3 blocks
                    return False
                # If no duplicates found, add the number to the corresponding set
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                blocks[(r//3,c//3)].add(board[r][c])
        
        # No duplicates ever found, return True
        # Note that the code does not evaluate if a sudoku board is solvable! Only checks if valid or not
        # Not all valid sudoku boards are solvable
        return True
