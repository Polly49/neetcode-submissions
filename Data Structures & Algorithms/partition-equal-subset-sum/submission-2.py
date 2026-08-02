class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        a=sum(nums)
        if a%2!=0:
            return False
        target=a//2
        def solve(ind,sm):
            if sm==target:
                return True

            if ind==len(nums) or sm>target:
                return False
            return (
                solve(ind+1,sm+nums[ind]) or 
                solve(ind+1,sm))
        return solve(0,0)