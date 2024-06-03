class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # d={}
        # for i in range(len(t)):
        #     for j in range(len(s)):
        #         if t[i]==s[j]:
        #             if t[i] in d:
        #                 d[t[i]].append(j)
        #             else:
        #                 d[t[i]]=[j]
        # print(d)
        # if len(d)==0:
        #     return len(t)
        # if len(d)==1:
        #     return len(t)-1
        
        
        svar=0
        tvar=0
        while svar<len(s) and tvar<len(t):
            if s[svar]==t[tvar]:
                tvar+=1
            svar+=1
        return len(t)-tvar
    
        