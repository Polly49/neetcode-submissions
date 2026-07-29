class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a=0
        dp={}
        def solve(sm):
            if sm in dp:
                return dp[sm]
            if sm==0:
                return 0
            if sm < 0:
                return float('inf')
            ans=float('inf')
            for n in coins:
                if sm-n>=0:
                    ans=min(ans,1+solve(sm-n))
            dp[sm] = ans
            return ans
            
        ans=solve(amount)
        if ans==float('inf'):
            return -1
        else:
            return ans
        


            
            

        