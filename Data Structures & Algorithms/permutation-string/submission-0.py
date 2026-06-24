class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=[0]*26
        b=[0]*26
        i=0
        j=0
        for k in range(0,len(s1)):
            a[ord(s1[k])-ord('a')]+=1
        while(j<len(s2)):
            b[ord(s2[j])-ord('a')]+=1        
            if j-i+1<len(s1):
                j+=1
            else:
                if a==b:
                    return True
                else:
                    b[ord(s2[i])-ord('a')]-=1
                    i+=1
                    j+=1
        return False
                    