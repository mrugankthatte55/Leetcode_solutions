class Solution:
    def totalMoney(self, n: int) -> int:
        k=n//7
        t1=28
        tn=28+(k-1)*7
        sn=k*(t1+tn)//2
        m=1+k
        l=0
        for i in range(n%7):
            l+=m+i
        return sn+l