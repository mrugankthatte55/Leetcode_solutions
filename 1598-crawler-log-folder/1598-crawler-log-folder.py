class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        for i in logs:
            if i=="./":
                continue
            if i=="../" and len(st)!=0:
                st.pop()
            elif i!="../":
                st.append(i)
            print(st)
        return len(st)