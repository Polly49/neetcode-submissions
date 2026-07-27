# class Solution:
#     def numDecodings(self, s: str):
#         dp=[-1]*(len(s)+1)
#         n=len(s)
#         dp[-1]=1
#         for i in range(n-1,-1,-1):
#             if s[i]=="0":
#                 dp[i]=0
#             dp[i]=dp[i+1]
#             if i+1<n:
#                 if s[i]=='1' or (s[i]=='2' and int(s[i+1])<7):
#                     dp[i]+=dp[i+2]
#         return dp[0]

class Solution:
    def numDecodings(self, s: str):
        n = len(s)
        dp = [0] * (n + 1)

        dp[n] = 1

        for i in range(n - 1, -1, -1):

            if s[i] == "0":
                dp[i] = 0
                continue

            dp[i] = dp[i + 1]

            if i + 1 < n and (
                s[i] == "1" or
                (s[i] == "2" and s[i + 1] <= "6")
            ):
                dp[i] += dp[i + 2]

        return dp[0]
        