class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def checkspec(i,j):
            if sum(mat[i])==1:
                s=0
                for x in range(len(mat)):
                    s+=mat[x][j]
                if s==1:
                    return True
            return False
        ans=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    if checkspec(i,j):
                        ans+=1
        return ans
