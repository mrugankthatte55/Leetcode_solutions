class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        arrdiff=[]
        ans=0
        n=len(nums1)
        
        for i in range(n):
            arrdiff.append(nums1[i]-nums2[i])
        arrdiff.sort()
        l = 0
        r = n - 1
        while l < r:
            if arrdiff[l]+arrdiff[r]>0:
                ans+=(r-l)
                r -= 1
            else:
                l += 1
            
        
        
        # for i in range(len(nums1)):
        #     for j in range(i+1,len(nums1)):
        #         if nums1[i]+nums1[j]>nums2[i]+nums2[j]:
        #             ans+=1
        return ans
        
        