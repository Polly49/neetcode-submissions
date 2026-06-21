class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        mx=0
        for r in range(0,len(prices)):
            if(prices[r]>prices[l]):
                mx=max(mx,prices[r]-prices[l])
            else:
                l=r
        return mx
            