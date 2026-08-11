class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def solve(ind,curr):
            if curr==target and ind==len(nums):
                return 1
            if ind>=len(nums):
                return 0
            if (ind,curr) in dp:
                return dp[(ind,curr)]
            
            cnt=0
            plus=solve(ind+1,curr+nums[ind])
            substraction=solve(ind+1,curr-nums[ind])
            dp[(ind,curr)]=plus+substraction 
            return dp[(ind,curr)]
        return solve(0,0)


