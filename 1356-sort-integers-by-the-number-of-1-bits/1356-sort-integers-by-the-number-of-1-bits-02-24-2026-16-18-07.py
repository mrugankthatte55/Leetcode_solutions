class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d={}
        for i in arr:
            n=bin(i)[2:].count('1')
            if n in d:
                d[n].append(i)
            else:
                d[n]=[i]
        ans=[]
        for n in d:
            a=sorted(d[n])
            for i in a:
                ans.append(i)

        # print(d)
        return ans