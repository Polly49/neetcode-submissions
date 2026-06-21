class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxr=[prices[-1]]*len(prices)
        mnl=[prices[0]]*len(prices)
        mx=0
        for i in range(1,len(prices)):
            if(prices[i]<mnl[i-1]):
                mnl[i]=prices[i]
            else:
                mnl[i]=mnl[i-1]
            
        for j in range(len(prices)-2,-1,-1):
            if(prices[j]>mxr[j+1]):
                mxr[j]=prices[j]
            else:
                mxr[j]=mxr[j-1]
        for i in range(0,len(prices)):
            mx=max(mx,mxr[i]-mnl[i])

        return mx
            