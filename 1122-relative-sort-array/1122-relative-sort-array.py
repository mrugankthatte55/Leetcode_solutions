class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d2={}
        for i in range (len(arr1)):
            if arr1[i] in d2:
                d2[arr1[i]]+=1
            else:
                d2[arr1[i]]=1
        ans=[]
        for i in arr2:
            for j in range(d2[i]):
                ans.append(i)
            d2[i]=0
        x=[]
        for i in d2:
            for j in range(d2[i]):
                x.append(i)
        x.sort()
        for i in x:
            ans.append(i)
        return ans