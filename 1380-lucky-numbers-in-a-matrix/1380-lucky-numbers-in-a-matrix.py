class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        c=[]
        for i in range(len(matrix[0])):
            m=matrix[0][i]
            for j in range(len(matrix)):
                if matrix[j][i]>m:
                    m=matrix[j][i]
            c.append(m)
        c=set(c)
        for i in matrix:
            x=min(i)
            if x in c:
                return [x]
        return []