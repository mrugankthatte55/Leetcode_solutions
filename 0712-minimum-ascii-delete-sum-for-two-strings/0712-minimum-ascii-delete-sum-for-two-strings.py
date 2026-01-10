class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        j = m - 1
        while j >= 0:
            dp[n][j] = dp[n][j + 1] + ord(s2[j])
            j -= 1

        i = n - 1
        while i >= 0:
            dp[i][m] = dp[i + 1][m] + ord(s1[i])
            i -= 1

        i = n - 1
        while i >= 0:
            j = m - 1
            while j >= 0:
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    delete_s1 = ord(s1[i]) + dp[i + 1][j]
                    delete_s2 = ord(s2[j]) + dp[i][j + 1]
                    dp[i][j] = min(delete_s1, delete_s2)
                j -= 1
            i -= 1

        return dp[0][0]
