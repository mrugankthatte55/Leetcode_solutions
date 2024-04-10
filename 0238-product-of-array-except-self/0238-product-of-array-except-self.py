class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prodLeft=[0]*n
        prodRight=[0]*n
        prodLeft[0]=1
        prodRight[n-1]=1
        for i in range(1,n):
            prodLeft[i]=prodLeft[i-1]*nums[i-1]
            prodRight[n-i-1]=prodRight[n-i]*nums[n-i]
        commonProd=[0]*n
        for i in range(n):
            commonProd[i]=prodLeft[i]*prodRight[i]
        return(commonProd)