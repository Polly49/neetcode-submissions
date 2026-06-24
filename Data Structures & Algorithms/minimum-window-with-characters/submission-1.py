class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need=Counter(t)
        window={}
        have=0
        need_count=len(need)
        i=0
        j=0
        res=[-1,-1]
        mn=float('inf')
        while(j<len(s)):
            if s[j] in need:
                window[s[j]]=1+window.get(s[j],0)
                if window[s[j]]==need[s[j]]:
                    have+=1
            while( have==need_count):
                # Update our result
                if (j-i+1) < mn:
                        mn = j-i+1
                        res = [i,j]
                # Keep shrinking our window because we want the minimum substring  
                if s[i] in window:
                    window[s[i]]-=1
                    if window[s[i]]<need[s[i]]:
                        have-=1
                
                i+=1
            j+=1
        if mn == float('inf'):
            return ""

        return s[res[0]:res[1]+1]



                
                

