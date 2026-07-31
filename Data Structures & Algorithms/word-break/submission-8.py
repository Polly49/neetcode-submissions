class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic=set(wordDict)
        dp={}
        def solve(start):
            if start in dp:
                return dp[start]
            if start==len(s):
                dp[start]=True
                return True
            for i in range(start,len(s)):
                if s[start:i+1] in dic:
                    if solve(i+1):
                        dp[start]=True
                        return True
            dp[start]=False
            return False
        return solve(0)
