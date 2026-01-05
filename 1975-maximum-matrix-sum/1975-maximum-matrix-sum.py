class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n=0
        s=0
        l=float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                s+=abs(matrix[i][j])
                if matrix[i][j]<=0:
                    n+=1
                if abs(matrix[i][j])<l:
                    l=abs(matrix[i][j])
        print(n)
        print(s)
        print(l)        
        if n%2==0:
            return s
        return s-2*l
