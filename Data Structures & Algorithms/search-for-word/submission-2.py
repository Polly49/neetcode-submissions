class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(i,j,substr,a):
            if (i,j) in a:
                return False
            sub=substr+board[i][j]
            if sub != word[:len(sub)]:
                return False
            if sub==word:
                return True
            a.add((i,j))        
            # Pick word in all Four Direction
            if j+1<len(board[0]):
                b=solve(i,j+1,sub,a)
                if b:
                    return True
            if i+1<len(board):
                b=solve(i+1,j,sub,a)
                if b:
                    return True
            if i-1>=0:
                b=solve(i-1,j,sub,a)
                if b:
                    return True
            if j-1>=0:
                b=solve(i,j-1,sub,a)
                if b:
                    return True    
            a.remove((i,j))        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if solve(i,j,"",set()):
                    return True   
        return False
        