class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            res = str(''.join(sorted(i)))
            if res in d:
                d[res].append(i)
            else:
                d[res]=[i]
        return(d.values())
        