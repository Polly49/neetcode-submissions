class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]
        for s in strs:
            b=[0]*26
            for i in s:
                b[ord(i)-ord("a")]+=1
            a.append(b)
        group={}
        for i in range(0,len(a)):
            g=tuple(a[i])
            if g not in group:
                group[g]=[]
            group[g].append(strs[i])
        

        
        return list(group.values())


            