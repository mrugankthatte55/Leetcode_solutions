class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==k:
            return nums
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return heapq.nlargest(k,d.keys(),key=d.get)
        # ans=[]
        # v=list(d.values())
        # v.sort(reverse='True')
        # print(v)
        # for i in range(len(v)-k):
        #     v.pop()
        # t=1
        # print(v)
        # for i in range(len(nums)-1):

        #     if nums[i]==nums[i+1]:
        #         t+=1
        #     else:
        #         if t in v:
        #             ans.append(nums[i])
        #             t=1
        #             print(t)
        # if t in v:
        #     ans.append(nums[i])
        #     t=1
        #     print(t)
        # d1={}
        # for i in d:
        #     d1[d[i]]=i
        # print(d)
        # print(d1)
        # f=list(d.values())
        # f.sort(reverse='True')
        # print(f)
        # ans=[]
        # for i in range(k):
        #     ans.append(d1[f[i]])
        # return ans