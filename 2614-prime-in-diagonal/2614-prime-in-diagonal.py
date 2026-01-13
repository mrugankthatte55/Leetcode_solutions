class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans=0
        n=len(nums)
        def isPrime(x):
            if x==1:
                return False
            for i in range(2,int(x**(0.5))+1):
                if x//i==x/i:
                    return False
            return True
        for i in range(n):
            # if nums[i][i]>ans:
            #     if isPrime(nums[i][i]):
            #         ans=nums[i][i]
            # if nums[i][n-1-i]>ans:
            #     if isPrime(nums[i][n-1-i]):
            #         ans=nums[i][n-1-i]

            if isPrime(nums[i][i]):
                ans=max(ans,nums[i][i])
            if isPrime(nums[i][n-i-1]):
                ans=max(ans,nums[i][n-1-i])
        return ans