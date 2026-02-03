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
            if nums[i]==nums[i-1]:
                return False
            elif nums[i]<nums[i-1]:
                if t==0:
                    t+=1
                if t==2:
                    return False
            elif nums[i]>nums[i-1] and t==1:
                t+=1
            i+=1
        if i==len(nums) and t==2:
            return True
        return False    

        

