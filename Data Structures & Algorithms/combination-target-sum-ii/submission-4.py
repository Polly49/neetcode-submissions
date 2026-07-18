class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates=sorted(candidates)
        def solve(i,sm,subset):
            if sm==target:
                res.append(subset.copy())
                return
            if i==len(candidates) or sm>target:
                return
            # Include Candidates[i]
            b=candidates[i]
            subset.append(b)
            solve(i+1,sm+b,subset)
            subset.pop()
            # Skip Candidates[i]
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            solve(i+1,sm,subset)
        solve(0,0,[])
        return res