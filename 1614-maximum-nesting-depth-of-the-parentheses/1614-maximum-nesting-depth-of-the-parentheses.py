class Solution:
    def maxDepth(self, s: str) -> int:
        # st=[]
        ans=0
        var1=0
        for i in range(len(s)):
            if s[i]=="(":
                var1+=1
            if s[i]==")":
                var1-=1
            ans=max(ans,var1)
        return ans
        # for i in range(len(s)):
        #     if s[i]=="(":
        #         st.append("(")
        #     if s[i]==")":
        #         st.pop()
        #     ans=max(ans,len(st))
        # return ans