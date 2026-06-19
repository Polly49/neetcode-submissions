class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Horizontal check
        
        for i in range(0,9):
            a=set()
            for j in range(0,9):
                if((board[i][j] in a) and board[i][j]!='.'):
                    return False
                else:
                    a.add(board[i][j])

        # Vertical Check
        for i in range(0,9):
            a=set()
            for j in range(0,9):
                if((board[j][i] in a) and board[j][i]!='.'):
                    return False
                else:
                    a.add(board[j][i])
        #  Sub Boxes Check
        # Row 1
        j=0
        while(j<9):
            a=set()
            for k in range(0,3):
                for l in range(0+j,3+j):
                    if ((board[k][l] in a) and board[k][l] !='.'):
                        return False
                    else:
                        a.add(board[k][l])
            j+=3
        # Row 2
        j=0
        while(j<9):
            a=set()
            for k in range(3,6):
                for l in range(0+j,3+j):
                    if ((board[k][l] in a) and board[k][l] !='.'):
                        return False
                    else:
                        a.add(board[k][l])
            j+=3
        #  Row 3
        j=0
        while(j<9):
            a=set()
            for k in range(6,9):
                for l in range(0+j,3+j):
                    if ((board[k][l] in a) and board[k][l] !='.'):
                        return False
                    else:
                        a.add(board[k][l])
            j+=3    
        

        # When all check done
        return True
            
            