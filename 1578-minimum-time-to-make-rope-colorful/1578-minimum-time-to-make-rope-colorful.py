class Solution(object):
    def minCost(self, col, time):
        n, ans = len(col), 0
        for i in range(1, n):
            if col[i] == col[i - 1]:
                ans += min(time[i], time[i - 1])
                time[i] = max(time[i], time[i - 1])
        return ans