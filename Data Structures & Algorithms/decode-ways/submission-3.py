class Solution:
    def numDecodings(self, s: str):
        dic = {}
        for i in range(1, 27):
            dic[str(i)] = chr(ord('A') - 1 + i)

        dp=[-1]*len(s)
        def solve(ind):
            if ind == len(s):
                return 1
            if s[ind]=="0":
                return 0
            
            if dp[ind]!=-1:
                return dp[ind]
            ways=0
            # One digit
            if s[ind] in dic:
                ways+=solve(ind + 1)
            
            # Two digits
            if ind + 1 < len(s):
                two = s[ind:ind+2]
                if two in dic:
                    ways+=solve(ind + 2)
            
            dp[ind]=ways
            return ways
        return solve(0)
                
                
        