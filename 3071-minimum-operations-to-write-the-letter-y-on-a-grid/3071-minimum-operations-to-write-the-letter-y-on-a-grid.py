class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n=len(grid)
        y=[0,0,0]
        nony=[0,0,0]
        # y=[]
        # nony=[]
        for i in range(n):
            for j in range(n):
                if ((i==j and i<=n//2) or (i<j and i+j==n-1) or (j==n//2 and i>n//2)):
                    # y.append(grid[i][j])
                    y[grid[i][j]]+=1
                else:
                    # nony.append(grid[i][j])
                    nony[grid[i][j]]+=1
        
        print(y)
        print(nony)
        
        return sum(y)+sum(nony)-max(y[0]+nony[1],y[0]+nony[2],y[1]+nony[0],y[1]+nony[2],y[2]+nony[1],y[2]+nony[0])
