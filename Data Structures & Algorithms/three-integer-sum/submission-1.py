class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a={}
        ans=[]
        nums=sorted(nums)
        for i in range(0,len(nums)):
            a[nums[i]]=i
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (-(nums[i]+nums[j]) in a) and (a[-nums[i]-nums[j]]>j ):
                    if [nums[i],nums[j],-(nums[i]+nums[j])] not in ans:
                        ans.append([nums[i],nums[j],-(nums[i]+nums[j])])
        return ans
