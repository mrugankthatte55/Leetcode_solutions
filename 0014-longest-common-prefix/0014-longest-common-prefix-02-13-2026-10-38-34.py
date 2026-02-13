class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        m=len(min(strs, key=len))
        print(strs)
        for i in range(1,m+1):
            s=set()
            for w in strs:
                s.add(w[0:i])
            if len(s)==1:
                for a in s:
                    ans=a
        return ans
