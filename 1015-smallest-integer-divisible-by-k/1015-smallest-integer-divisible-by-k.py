class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        n=1
        for i in range (1,k+1):
            if n%k==0:
                return i
            n*=10
            n+=1
        return -1
        