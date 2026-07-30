class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic=set(wordDict)
        dp={}
        def solve(start):
            if start in dp:
                return dp[start]
            if start==len(s):
                return True
            for end in range(start,len(s)):
                if s[start:end+1] in dic:
                    if solve(end+1):
                        dp[start]=True  
                        return True
            dp[start]=False

                        
        solve(0)
        return dp[0]  
