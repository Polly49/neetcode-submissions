class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def solve(sm):
            if sm in dp:
                return dp[sm]
            if sm==1:
                dp[sm]=1
                return 1
            elif sm==2:
                dp[sm]=2
                return 2
            dp[sm]=solve(sm-1)+solve(sm-2) 
            return dp[sm]
        return solve(n)
