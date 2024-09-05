class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing=(mean*(n+len(rolls)))-sum(rolls)
        if missing > 6*n or missing<n:
            return []
        ans=[missing//n]*n
        missing2=missing-sum(ans)
        # print(missing2)
        # if missing2<0:
        #     return []
        for i in range(missing2):
            ans[i%n]+=1
        # if max(ans)>6:
        #     return []
        return ans        
    