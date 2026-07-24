class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(i,j,k,a):
            if (i,j) in a:
                return False
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            a.add((i,j))        
            # Pick word in all Four Direction
            if j+1<len(board[0]):
                b=solve(i,j+1,k+1,a)
                if b:
                    return True
            if i+1<len(board):
                b=solve(i+1,j,k+1,a)
                if b:
                    return True
            if i-1>=0:
                b=solve(i-1,j,k+1,a)
                if b:
                    return True
            if j-1>=0:
                b=solve(i,j-1,k+1,a)
                if b:
                    return True    
            a.remove((i,j))        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if solve(i,j,0,set()):
                    return True   
        return False
        