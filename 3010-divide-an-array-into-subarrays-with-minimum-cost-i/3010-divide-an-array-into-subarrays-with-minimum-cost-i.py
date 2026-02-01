class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans=nums[0]
        min1=51
        min2=51
        for i in nums[1:len(nums)]:
            if i <= min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
        return ans+min1+min2
        
        # nums=sorted(nums[1:len(nums)])
        # return nums[0]+nums[1]+ans