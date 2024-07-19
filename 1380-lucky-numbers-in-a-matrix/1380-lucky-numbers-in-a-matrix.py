class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        r=[]
        c=[]
        for i in matrix:
            r.append(min(i))
        for i in range(len(matrix[0])):
            m=matrix[0][i]
            for j in range(len(matrix)):
                if matrix[j][i]>m:
                    m=matrix[j][i]
            c.append(m)
        c=set(c)
        for i in matrix:
            if min(i) in c:
                return [min(i)]
        return []