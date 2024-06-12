class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # arr=[0,0,0]
        # for i in range(len(nums)):
        #     arr[nums[i]]+=1
        # # print(arr)
        # for i in range(len(nums)):
        #     if arr[0]!=0:
        #         nums[i]=0
        #         arr[0]-=1
        #     elif arr[1]!=0:
        #         nums[i]=1
        #         arr[1]-=1
        #     elif arr[2]!=0:
        #         nums[i]=2
        #         arr[2]-=1
        nums.sort()