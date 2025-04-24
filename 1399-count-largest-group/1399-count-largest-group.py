class Solution:
    

    def countLargestGroup(self, n: int) -> int:
        def sumofdigits(num):
            s=0
            while num>0:
                s+=num%10
                num=num//10
            return s
        d={}
        for i in range(1,n+1):
            s=sumofdigits(i)
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        v=d.values()
        ans=0
        for i in v:
            if i==max(v):
                ans+=1
        return ans