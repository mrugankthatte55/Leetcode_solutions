class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1: return False
        
        nums[0] %= k
        for i in range(1, len(nums)):
            nums[i] = (nums[i-1] + nums[i]) % k

        seen = set()
        l, r = 0, 1
        while r < len(nums):
            if nums[r] == 0 or nums[r] in seen:
                return True
            seen.add(nums[l])
            l, r = l+1, r+1
        return False