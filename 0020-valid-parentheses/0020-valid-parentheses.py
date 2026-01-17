class Solution:
    def isValid(self, s: str) -> bool:
        left=['(','{','[']
        right=[')','}',']']
        st=[]
        for c in s:
            if c in left:
                st.append(c)
            else:
                if len(st)==0:
                    return False
                i=right.index(c)
                if st[-1]==left[i]:
                    st.pop()
                else:
                    return False
        if len(st)!=0:
            return False
        return True