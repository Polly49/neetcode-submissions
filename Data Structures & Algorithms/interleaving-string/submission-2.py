class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=len(s1)+len(s2):
            return False
        dp={}
        def solve(i,j,curr):
            if (i,j) in dp:
                return dp[(i,j)]
            if len(curr)>0 and curr[i+j-1]!=s3[i+j-1]: 
                return False
            if curr==s3:
                return True
            if i>=len(s1) and j>=len(s2):
                return False
            if i<len(s1):
                if solve(i+1,j,curr+s1[i]):
                    dp[(i+1,j)]=True
                    return True
            if j<len(s2):
                if solve(i,j+1,curr+s2[j]):
                    dp[(i,j+1)]=True
                    return True
            dp[(i,j)]=False
            return False
        return solve(0,0,"")

        
                
        