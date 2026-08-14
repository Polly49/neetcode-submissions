class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp={}
        def solve(ind,substring):
            if substring==t:
                return 1
            if ind>=len(s):
                return 0
            if(ind,substring) in dp:
                return dp[(ind,substring)]
            pick=solve(ind+1,substring+s[ind])
            not_pick=solve(ind+1,substring)
            dp[(ind,substring)]=pick+not_pick
            return dp[(ind,substring)]
        return solve(0,"")
        
                