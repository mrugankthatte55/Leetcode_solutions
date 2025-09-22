class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=d.values()
        m=max(c)
        fre=0
        for i in c:
            if i==m:
                fre+=1
        return fre*m