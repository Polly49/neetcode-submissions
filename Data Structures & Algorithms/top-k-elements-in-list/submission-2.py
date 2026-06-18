class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for n in nums:
            if n in a:
                a[n]+=1
            else:
                a[n]=1
        b=sorted(a.items(),key=lambda x:x[1],reverse=True)[:k]
        ans=[num for num,count in b]
        return ans
