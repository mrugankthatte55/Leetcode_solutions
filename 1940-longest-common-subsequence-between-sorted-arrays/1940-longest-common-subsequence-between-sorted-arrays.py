class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        x=len(arrays)
        ans=[]
        d={}
        for i in arrays:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        for i in d:
            if d[i]==x:
                ans.append(i)
        return(ans)
        
        # for i in arrays[0]:
        #     for j in arrays[1]:
        #         if i==j:
        #             x.append(i)
        # if len(arrays)==2:
        #     return x
        # print(x)
        # for i in range(2,len(arrays)):
        #     newx=x
        #     for y in x:
        #         if y not in arrays[i]:
        #             newx.remove(y)
        #     x=newx
        #     print(x)
        #     print(newx)
        # return x
    
     # 1 2 3 6 9
     # 2 3 9
     # 3 9