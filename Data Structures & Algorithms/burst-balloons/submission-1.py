class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp={}
        def func(nums,ind):
            if len(nums)==1:
                return nums[0]
            elif ind==0:
                return nums[ind]*nums[ind+1]
            elif ind==len(nums)-1:
                return nums[ind-1]*nums[ind]

            return nums[ind-1]*nums[ind]*nums[ind+1]
        def solve(nums):
            if len(nums)<=1:
                return nums[0]
            if tuple(nums) in dp:
                return dp[tuple(nums)]
            ans=float('-inf')
            for i in range(len(nums)):
                temp=nums
                temp=nums[:i]+nums[i+1:]
                ans=max(ans,func(nums,i)+solve(temp))
            dp[tuple(nums)]=ans
            return ans  
        return solve(nums)
            