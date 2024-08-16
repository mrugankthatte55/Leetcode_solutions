class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        ans = 0
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        
        for i in range(1, len(arrays)):
            ans = max(ans, max(abs(arrays[i][-1] - minVal), abs(maxVal - arrays[i][0])))
            minVal = min(minVal, arrays[i][0])
            maxVal = max(maxVal, arrays[i][-1])
        
        return ans
        
        
        
        # mdist=0
        # minArr={}
        # maxArr={}
        # newArr=[]
        # for i in range(len(arrays)):
        #     newArr.append([arrays[i][0],arrays[i][-1]])
            
            # newArr.append(min(arrays[i]))
            # newArr.append(max(arrays[i]))
            # minArr[i]=min(arrays[i])
            # maxArr[i]=max(arrays[i])
        
        # newArr.sort()
        # n=len(newArr)
        # for i in range(n//2):
        #     if 
        
        # [[1,3],[4,5],[1,3]]
        # [1,1,2,2,3,3,4,5]
        