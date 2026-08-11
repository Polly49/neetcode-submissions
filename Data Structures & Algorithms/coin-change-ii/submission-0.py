class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        def solve(i,amount):
            if amount==0:
                return 1
            if amount<0 or i>=len(coins):
                return 0
            if (i,amount) in dp:
                return dp[(i,amount)]
            cnt=0
            # Pick
            take= solve(i,amount-coins[i])
            skip= solve(i+1,amount)
            dp[(i,amount)]=take+skip
            return dp[(i,amount)]
        return solve(0,amount) 
        