class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        s=s.replace(" ","")
        j=len(s)-1
        while(i<j):
            while i<j and (not s[i].isalnum()):
                i+=1
            
            while i<j and (not s[j].isalnum()):
                j-=1
            
            if(s[i].lower()!=s[j].lower() and i<j):
                return False
            else:
                i+=1
                j-=1
            
        return True