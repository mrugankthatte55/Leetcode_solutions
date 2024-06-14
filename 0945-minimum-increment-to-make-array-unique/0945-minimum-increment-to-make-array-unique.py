class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        min_increments = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] + 1 - nums[i]
                min_increments += increment
                nums[i] = nums[i - 1] + 1
        return min_increments
        # d={}
        # s=sum(nums)
        # for i in nums:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # # print(d)
        # # return 1
        # f=0
        # while f==0:
        #     if set(d.values())=={1}:
        #         f=1
        #         return sum(nums)-s
        #     for i in range(len(nums)):
        #         # print(nums)
        #         if d[nums[i]]>1:
        #             d[nums[i]]-=1
        #             nums[i]+=1
        #             if nums[i] in d:
        #                 d[nums[i]]+=1
        #             else:
        #                 d[nums[i]]=1
        
                    
                