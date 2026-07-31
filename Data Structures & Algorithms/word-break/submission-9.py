class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)
        dp[-1]=True
        for start in range(n-1,-1,-1):
            for end in range(start,n):
                if s[start:end+1] in dic:
                    if dp[end+1]:
                        dp[start]=True

        return dp[0]
