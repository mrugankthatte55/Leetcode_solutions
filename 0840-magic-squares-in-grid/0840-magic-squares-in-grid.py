class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def checkMagic(mat: List[List[int]]):
            s=set([])
            for i in mat:
                for j in i:
                    s.add(j)
            if s!={1,2,3,4,5,6,7,8,9}:
                return False
            r1=sum(mat[0])
            r2=sum(mat[1])
            r3=sum(mat[2])
            
            d1=mat[0][0]+mat[1][1]+mat[2][2]
            d2=mat[0][2]+mat[1][1]+mat[2][0]
            
            c1=mat[0][0]+mat[1][0]+mat[2][0]
            c2=mat[0][1]+mat[1][1]+mat[2][1]
            c3=mat[0][2]+mat[1][2]+mat[2][2]
            
            if r1==r2==r3==d1==d2==c1==c2==c3:
                return True
            return False
        ans=0
        n=len(grid)
        m=len(grid[0])
        if n<3 or m<3:
            return ans

        ans=0
        for i in range(n-2):
            for j in range(m-2):
                mat=[]
                for k in range(3):
                    temp=[]
                    for l in range(3):
                        temp.append(grid[i+k][j+l])
                    mat.append(temp)
                # mat=[[grid[i][j], grid[i][j+1], grid[i][j+2]], [grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]], [grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]]
                if checkMagic(mat):
                    ans+=1
        return ans
        
        