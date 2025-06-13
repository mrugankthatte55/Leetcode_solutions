class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1])>ans:
                ans=abs(nums[i]-nums[i+1])
        if abs(nums[0]-nums[-1])>ans:
            ans=abs(nums[0]-nums[-1])
        return ans