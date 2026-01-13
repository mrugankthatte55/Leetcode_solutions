class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # newarr=[]
        # for i in nums:
        #     newarr.append(target-i)
        
        # for i in range(len(nums)):
        #     newarr[i]+=nums[i]
        # print(newarr)
        # return []
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        for i in range(len(nums)):
            if target-nums[i] in d:
                for j in d[target-nums[i]]:
                    if j!=i:
                        return [i,j]
        # print(d)
        # print(nums)
        # return []