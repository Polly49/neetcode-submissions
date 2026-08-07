class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp={}
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==m-1 and j==n-1:
                return 1
            # k=0 from the top
            # k=1 from the left
            # k=2 from the right
            # k=3 from the bottom
            cnt=0
            # Towards right
            if j!=n-1 :
                cnt+=solve(i,j+1) 
            # Towards bottom
            if i!=m-1:
                cnt+=solve(i+1,j)
            dp[(i,j)]=cnt
            return dp[(i,j)]
        return solve(0,0)
        