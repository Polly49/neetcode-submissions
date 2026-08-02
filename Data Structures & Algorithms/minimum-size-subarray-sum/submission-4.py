class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,0
        n=len(nums)
        sm=0
        ans=float('inf')
        while (j<n):
            sm=sm+nums[j]
            if sm<target:
                j+=1
            elif sm>=target:
                while sm>=target:
                    ans=min(ans,j-i+1)
                    sm-=nums[i]
                    i+=1
                
                j+=1

        if ans==float('inf'):
            return 0
        else:
            return ans
