class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        d={}
        for s in strs:
            s1="".join(sorted(s))
            if s1 in d:
                d[s1].append(s)
            else:
                d[s1]=[s]
        print(d.values())
        return list(d.values())
        
