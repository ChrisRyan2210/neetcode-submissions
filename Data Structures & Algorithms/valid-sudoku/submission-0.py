class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # for rows/cols we can use range(9) as they are always 9x9
        # we should use sets as our cols/rows 
        
        # create sets for us to insert into
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # loop through each row/col
        for r in range(9):
            for c in range(9):
                # skip cells where value = '.'
                if board[r][c] == '.':
                    continue
                # if value already in one of the sets, return False
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                # otherwise, add the cell to the sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True
