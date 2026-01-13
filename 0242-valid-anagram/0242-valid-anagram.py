class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s)==sorted(t):
        #     return True
        # return False
        if len(s)!=len(t):
            return False
        ds={}


        for i in range(len(s)):
            if s[i] in ds:
                ds[s[i]]+=1
            else:
                ds[s[i]]=1
        for i in range(len(t)):
            if t[i] in ds:
                ds[t[i]]-=1
            else:
                return False
        # print(ds.values())
        # print(set(ds.values()))
        if set(ds.values())=={0}:
            return True
        return False