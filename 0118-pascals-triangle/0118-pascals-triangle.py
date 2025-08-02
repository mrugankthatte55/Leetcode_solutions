class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1],[1,1]]
        for i in range (numRows-2):
            print(i)
            t=[1]
            for j in range(len(ans[-1])-1):
                t.append(ans[-1][j]+ans[-1][j+1])




            t.append(1)
            ans.append(t)
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        return ans
