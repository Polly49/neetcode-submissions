class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*26
        b=[0]*26
        for c in s:
            a[ord(c)-ord('a')]+=1
        for d in t:
            b[ord(d)-ord('a')]+=1
        if a==b:
            return True
        else:
            return False 