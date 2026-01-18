class Solution:
    def isHappy(self, n: int) -> bool:
        def sumsq(n):
            s=0
            while n>0:
                s+=(n%10)**2
                n=n//10
            return s
        visited=set()
        while n not in visited:
            visited.add(n)
            n=sumsq(n)

            if n==1:
                return True
        return False