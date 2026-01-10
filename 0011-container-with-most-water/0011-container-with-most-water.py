class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        maxar=0
        def calcarea(i,j):
            return min(height[i],height[j])*(j-i)
        if n<=1:
            return 0
        i,j=0,n-1
        while i<j:
            maxar=max(maxar,calcarea(i,j))
            print(i,j,maxar)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxar
        

            
