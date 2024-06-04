class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        ans=0
        f=1
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]%2==0:
                ans+=d[i]
            else:
                ans+=(d[i]-1)
                f=0
        if f==0:
            return ans+1
        return ans