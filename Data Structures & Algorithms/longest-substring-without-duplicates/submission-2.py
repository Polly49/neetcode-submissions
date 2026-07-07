class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        i=0
        j=0
        mx=0
        while(j<len(s)):
            if s[j] not in a:
                a.add(s[j])
                mx=max(mx,j-i+1)
                j+=1
            else:
                while(s[j] in a):
                    a.discard(s[i])
                    i+=1

        return mx


            
                 