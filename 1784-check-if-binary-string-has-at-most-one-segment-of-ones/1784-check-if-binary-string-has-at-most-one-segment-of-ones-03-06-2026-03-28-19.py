class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s=="1":
            return True
        f=1
        for i in range(1,len(s)):
            # if s[i]=='1' and f==0:
            #     f=1
            if s[i]=='0' and f==1:
                f=2
            if s[i]=="1" and f==2:
                return False
        return True