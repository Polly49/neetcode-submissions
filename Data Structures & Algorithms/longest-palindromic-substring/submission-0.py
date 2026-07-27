class Solution:
    def check(self,s):
        return s==s[::-1]
    def longestPalindrome(self, s: str) -> str:
        curr=""
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if self.check(s[i:j+1]):
                    if len(curr)<=j-i+1:
                        curr=s[i:j+1]
        return curr
        
            