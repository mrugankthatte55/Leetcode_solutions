class Solution:
    def climbStairs(self, n: int) -> int:
        d={}
        def steps(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 2
            else:
                if n in d:
                    return d[n]
                d[n]=steps(n-1)+steps(n-2)
                return d[n]
        return steps(n)