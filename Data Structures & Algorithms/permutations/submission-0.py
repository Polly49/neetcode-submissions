class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        def solve(subset):
            if len(subset)==len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # explore
                subset.append(nums[i])
                used[i]=True

                # recall
                solve(subset)

                # popout
                subset.pop()
                used[i]=False
        solve([])

        return res    