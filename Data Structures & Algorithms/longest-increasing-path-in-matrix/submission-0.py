class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}
        n=len(matrix)   #Rows
        m=len(matrix[0]) #Columns
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if (i>=n or j>=m) or (i<0 or j<0):
                return 0
            ans=1
            curr=matrix[i][j]
            if i-1>=0 and matrix[i-1][j]>curr:
                # Move Up
                ans=max(ans,1+solve(i-1,j))
            if i+1<n and matrix[i+1][j]>curr:
                # Move Down
                ans=max(ans,1+solve(i+1,j))
            if j-1>=0 and matrix[i][j-1]>curr: 
                # Move left
                ans=max(ans,1+solve(i,j-1))
            if j+1<m and matrix[i][j+1]>curr:
                # Move right
                ans=max(ans,1+solve(i,j+1))
            dp[(i,j)]=ans
            return dp[(i,j)]
        ans=-1
        for i in range(n):
            for j in range(m):
                ans=max(ans,solve(i,j))
        return ans