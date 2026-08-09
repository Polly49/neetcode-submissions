class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[None]*len(nums)
        def solve(ind):
            if ind>=len(nums)-1:
                return True
            if dp[ind] is not None:
                return dp[ind]
            if nums[ind]==0:
                return False
            for i in range(1,nums[ind]+1):
                if solve(ind+i):
                    dp[ind]=True
                    return True
            dp[ind]=False
            return False
        return solve(0)
            