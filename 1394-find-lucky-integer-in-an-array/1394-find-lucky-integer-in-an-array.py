class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=[]
        for i in d:
            if d[i]==i:
                ans.append(i)
        if len(ans)==0:
            return -1
        return max(ans)