class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        t=sum(apple)
        capacity.sort(reverse=True)
        ans=0
        for i in capacity:
            if t<=0:
                return ans
            t-=i
            ans+=1
        return ans
            

