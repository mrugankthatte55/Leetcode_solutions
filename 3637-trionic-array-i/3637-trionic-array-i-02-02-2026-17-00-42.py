class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums)==3:
            return False
        if nums[1]<=nums[0]:
            return False
        if nums[-1]<=nums[-2]:
            return False
        i=1
        t=0
        while i<=len(nums)-1:
            # print(i)
            # print(t)
            if nums[i]==nums[i-1]:
                return False
            elif nums[i]<nums[i-1] and t==0:
                t+=1
            elif nums[i]>nums[i-1] and t==1:
                t+=1
            elif nums[i]<nums[i-1] and t==2:
                return False
            i+=1
        # print(t)
        # print(i)
        if i==len(nums) and t==2:
            return True
        return False    

        

