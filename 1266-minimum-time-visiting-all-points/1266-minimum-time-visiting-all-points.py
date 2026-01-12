class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 0
        ans=0
        cur=points[0]
        for i in range(1,len(points)):
            x=abs(points[i][0]-cur[0])
            y=abs(points[i][1]-cur[1])
            ans+=max(x,y)
        return ans




