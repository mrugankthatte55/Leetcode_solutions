class Solution:
    def maxFreqSum(self, s: str) -> int:
        v={'a':0,'e':0,'i':0,'o':0,'u':0}
        c={}
        for i in s:
            if i in v:
                v[i]+=1
            else:
                if i in c:
                    c[i]+=1
                else:
                    c[i]=1
        return max(v.values()) + (max(c.values()) if c else 0)