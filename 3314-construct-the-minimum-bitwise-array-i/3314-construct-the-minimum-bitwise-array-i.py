class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        def findans(n):
            for i in range(n):
                if (i+1)|i==n:
                    return i
            return -1
        for i in range(len(nums)):
            ans.append(findans(nums[i]))
        return ans