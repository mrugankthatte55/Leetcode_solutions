class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        n=len(nums)
        l=(n//2)-1
        r=n//2
        for i in range(n//2):
            if nums[l-i]+nums[r+i]>=ans:
                ans=max(ans,nums[l-i]+nums[r+i])
            else:
                return ans
        return ans

