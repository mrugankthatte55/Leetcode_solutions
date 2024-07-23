class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        vals=sorted(set(d.values()))
        ans=[]
        for i in vals:
            temp=[]
            for j in d:
                if d[j]==i:
                    temp.append(j)
            temp.sort(reverse=True)
            for k in temp:
                for l in range(d[k]):
                    ans.append(k)
            # print(temp)
        # print (vals)
        return ans