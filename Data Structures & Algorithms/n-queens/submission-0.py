class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        res=[]
        a=set()
        b=set()
        cols=set()
        def check(row,col,a,b):
            if row-col in a or row+col in b:
                return False
            elif col in cols:
                return False
            else:
                return True
        def solve(board,row):
            if row==n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                if check(row,col,a,b):
                    # Place Queen
                    board[row][col]="Q"
                    cols.add(col)
                    a.add(row-col)
                    b.add(row+col)
                    # Call for next
                    solve(board,row+1)
                    # Remove Queen
                    board[row][col]="."
                    cols.discard(col)
                    a.discard(row-col)
                    b.discard(row+col)

        solve(board,0)
        return res