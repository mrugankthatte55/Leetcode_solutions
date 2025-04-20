class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d={}
        for i in answers:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=0
        for i in d:
            ans += math.ceil(d[i]/(i+1))*(i+1)
        return ans