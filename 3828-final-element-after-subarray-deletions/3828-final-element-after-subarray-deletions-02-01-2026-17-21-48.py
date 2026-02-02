class Solution:
    def finalElement(self, nums: List[int]) -> int:
        # 1, 2, 6, 10, 20, 4, 7, 5
        # 1, 2, 4, 5, 6, 7, 10, 20

        # 42, 23,55,65,7,30,1,59
        # 1, 7, 23, 30, 42, 55, 59, 65

        # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        # 10, 2, 9, 3, 4, 6, 5, 7, 1, 8 
        return max(nums[0],nums[-1])