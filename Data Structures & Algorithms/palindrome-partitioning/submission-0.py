class Solution:
    def check(self,s):
        if s==s[::-1]:
            return True
        else:
            return False
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def solve(start,subset):
            if start==len(s):
                res.append(subset.copy())
                return
            for end in range(start,len(s)):
                if self.check(s[start:end+1]):
                    subset.append(s[start:end+1])
                    solve(end+1,subset)
                    subset.pop()
        solve(0,[])
        return res
            
