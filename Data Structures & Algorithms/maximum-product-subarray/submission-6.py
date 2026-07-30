class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        currMin,currMax=1,1
        for n in nums:
            if n==0:
                currMin=1
                currMax=1
                continue
            temp1=currMax*n
            temp2=currMin*n
            currMax=max(temp1,temp2,n)
            currMin=min(temp1,temp2,n)
            res=max(res,currMax)
        return res