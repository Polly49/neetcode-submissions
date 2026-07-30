class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for start in range(len(s)-1, -1, -1):
            for end in range(start+1, len(s)+1):

                if s[start:end] in dic and dp[end]:
                    dp[start] = True
                    break

        return dp[0]