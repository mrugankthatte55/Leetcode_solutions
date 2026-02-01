class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans=nums[0]
        nums=sorted(nums[1:len(nums)])
        # print(nums)
        # return 0
        return nums[0]+nums[1]+ans
        # for i in range(1,len(nums)):
        #     5, 6, 7, 8, 2, 9, 10, 3