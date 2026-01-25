class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 9 7 4 1 
        # n=7
        # k=6
        nums.sort(reverse='true')
        print(nums)
        return nums[0]-nums[k-1]