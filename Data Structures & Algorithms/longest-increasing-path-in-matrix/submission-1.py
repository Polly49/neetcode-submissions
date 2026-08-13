class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}
        n=len(matrix)  #Rows
        m=len(matrix[0]) #Columns
        def solve(i,j,prev):
            if (i>=n or j>=m) or (i<0 or j<0):
                return 0
            if prev>=matrix[i][j]:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            ans=1
            prev=matrix[i][j]
            # Move Up
            up=1+solve(i-1,j,prev)
            # Move Down
            down=1+solve(i+1,j,prev)
            # Move left
            left=1+solve(i,j-1,prev)
            # Move right
            right=1+solve(i,j+1,prev)
            ans=max(ans,up,down,right,left)
            dp[(i,j)]=ans
            return dp[(i,j)]
        ans=-1
        for i in range(n):
            for j in range(m):
                ans=max(ans,solve(i,j,float('-inf')))
        return ans
