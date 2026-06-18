class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward=[0]*len(nums)
        backward=[0]*len(nums)
        ans=[0]*len(nums)
        forward[0]=1
        backward[-1]=1
        multiple=1
        for i in range(1,len(nums)):
            multiple=multiple*nums[i-1]
            forward[i]=multiple
        multiple=1
        for j in range(len(nums)-2,-1,-1):
            multiple=multiple*nums[j+1]
            backward[j]=multiple
        for j in range(0,len(nums)):
            ans[j]=forward[j]*backward[j]
            
        return ans
