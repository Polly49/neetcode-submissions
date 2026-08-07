class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        def solve(ind1,ind2):
            if (ind1,ind2) in dp:
                return dp[(ind1,ind2)]
            if ind1<0 or ind2<0:
                return 0
            if text1[ind1]==text2[ind2]:
                dp[(ind1,ind2)]=1+solve(ind1-1,ind2-1)
                return 1+solve(ind1-1,ind2-1)
            dp[(ind1,ind2)]=max(solve(ind1-1,ind2),solve(ind1,ind2-1))
            return max(solve(ind1-1,ind2),solve(ind1,ind2-1))
        return solve(len(text1)-1,len(text2)-1)