class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n1=[]
        n2=[]
        for i in range(1,n+1):
            if i%m==0:
                n2.append(i)
            else:
                n1.append(i)
        return sum(n1)-sum(n2)