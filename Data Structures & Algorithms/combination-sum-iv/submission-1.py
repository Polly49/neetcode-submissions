class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp={}
        def solve(sm):
            if sm in dp:
                return dp[sm]
            if sm==target:
                return 1
            if sm>target:
                return 0
            ans=0

            for num in nums:
                ans+=solve(num+sm)
            dp[sm]=ans
            return dp[sm]
            
        return solve(0)
        