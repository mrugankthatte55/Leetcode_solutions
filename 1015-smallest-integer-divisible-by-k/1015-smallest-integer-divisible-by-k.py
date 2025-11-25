class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        n=1
        if n%k==0:
            return 1
        for i in range (2,k+1):
            n*=10
            n+=1
            if n%k==0:
                return i
        return -1
        