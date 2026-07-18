class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        a=nums
        def solve(i,sm,subset):
            if sm==target:
                res.append(subset.copy())
                return
            if i>=len(nums) or sm>target:
                return
            b=nums[i]
            subset.append(b)
            solve(i,sm+b,subset)

            subset.pop()
            solve(i+1,sm,subset)
        solve(0,0,[])
        return res

