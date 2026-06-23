class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mx=0
        a=[0]*26
        i=0
        j=0
        while(j<len(s)):
            a[ord(s[j])-ord('A')]+=1
            if j-i+1-max(a)<=k:
                mx=max(mx,j-i+1)
                j+=1
            else:
                while (j-i+1)-max(a)>k:
                    a[ord(s[i])-ord('A')]-=1
                    i+=1
                j+=1
        return mx