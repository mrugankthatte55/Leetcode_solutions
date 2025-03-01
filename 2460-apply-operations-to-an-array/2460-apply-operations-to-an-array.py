class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        c=0
        arr=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                arr.append(nums[i])
            else:
                c+=1
        for i in range(c):
            arr.append(0)

        return arr
        