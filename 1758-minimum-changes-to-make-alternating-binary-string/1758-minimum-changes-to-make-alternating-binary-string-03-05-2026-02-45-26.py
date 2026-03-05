class Solution:
    def minOperations(self, s: str) -> int:
        def ops(sres):
            ans=0
            for i in range(len(s)):
                if sres[i]!=s[i]:
                    ans+=1
            return ans
        s1=""
        s2=""
        for i in range(len(s)):
            if i%2==0:
                s1+='0'
                s2+='1'
            else:
                s1+='1'
                s2+='0'
        return min(ops(s1),ops(s2))    
        
        