class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        a = [False, False] + [True] * (n - 2)
        for i in range(2, int(sqrt(n)) + 1):
            if a[i]:
                for j in range(i * i, n, i):
                    a[j] = False
        return sum(a)