class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def solve(subset,l,r):
            if len(subset)==2*n:
                res.append(subset)
                return
            if l<=r:
                subset=subset+"("
                l+=1
                solve(subset,l,r)
            elif l>r:
                if l<n:
                    solve(subset+"(",l+1,r)
                    solve(subset+")",l,r+1)
                elif l==n:
                    solve(subset+")",l,r+1)
        solve("",0,0)
        return res
        