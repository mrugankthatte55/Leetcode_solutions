class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=[]
        ans=0
        for i in s:
            if a and a[-1] == "b" and i == "a":
                a.pop()
                ans += 1
            else:
                a.append(i)
        return ans