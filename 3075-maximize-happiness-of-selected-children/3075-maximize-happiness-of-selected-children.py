class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        h=0
        t=0
        for i in range(0,len(happiness)):
            if t==k:
                return h
            if happiness[i]-t<0:
                return h
            h+=happiness[i]-t
            t+=1
        return h