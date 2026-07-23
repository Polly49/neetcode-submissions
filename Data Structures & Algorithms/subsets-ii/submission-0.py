class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res=[]
        a=set()
        def solve(ind,subset,a):
            if ind>=len(nums):
                res.append(subset.copy())
                return 
            #Pick
            subset.append(nums[ind])
            # recall
            solve(ind+1,subset,a)
            # undo
            subset.pop()
            while ind+1<len(nums) and nums[ind]==nums[ind+1]:
                ind+=1
            solve(ind+1,subset,a)
        solve(0,[],a)
        return res