class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        weights=[0]*n
        for i in roads:
            weights[i[0]]+=1
            weights[i[1]]+=1
        print(weights)
        weights.sort()
        for i in range(n):
            weights[i]=weights[i]*(i+1)
        return sum(weights)
        
        

    