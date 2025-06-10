class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # max odd - min even
        a1=0
        a2=200
        for i in d.values():
            if i%2==0:
                if i<a2:
                    a2=i
            else:
                if i>a1:
                    a1=i
        return a1-a2
