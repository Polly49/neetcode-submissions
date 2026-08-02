class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        a=sum(nums)
        if a%2!=0:
            return False
        target=a//2
        def solve(ind,sm):
            if sm==target:
                return True
            if ind==len(nums):
                return False
            for i in range(ind,len(nums)):
                if sm>target:
                    return False
                sm=sm+nums[i]
                if solve(i+1,sm):
                    return True
                sm=sm-nums[i]
            return False
        return solve(0,0)