class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for n in strs:
            a=len(n)
            string=string +f'{a}' + "|" +n
        return str(string)
    def decode(self, s: str) -> List[str]:
        decode=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!='|'):
                j+=1
            length=int(s[i:j])
            i=j+1+length
            string=s[j+1:j+1+length]
            decode.append(string)
            
        return decode
