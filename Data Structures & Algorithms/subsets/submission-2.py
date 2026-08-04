class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def solve(ind,subset):
            if ind>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[ind])    
            # Pick
            solve(ind+1,subset)
            # Pop for Not Pick
            subset.pop()
            # Call for Not Pick
            solve(ind+1,subset)
        solve(0,[])
        return res