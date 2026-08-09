class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def solve(ind,canbuy):
            if (ind,canbuy) in dp:
                return dp[(ind,canbuy)]
            if ind>=len(prices):
                return 0
            sm=0
            if canbuy:
                buy=-prices[ind]+solve(ind+1,0)
                skip=solve(ind+1,1)
                dp[(ind,canbuy)]=max(buy,skip)
            else:
                sell=prices[ind]+solve(ind+2,1)
                skip=solve(ind+1,0)
                dp[(ind,canbuy)]=max(sell,skip)
            return dp[(ind,canbuy)]
        return solve(0,1)