class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt=[0]*max(nums)
        for i in range(len(nums)):
            cnt[nums[i]-1]+=1
        for i in cnt:
            if i%2!=0:
                return False
        return True