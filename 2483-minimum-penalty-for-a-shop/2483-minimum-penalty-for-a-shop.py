class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ypen=[0]*(n+1)
        npen=[0]*(n+1)
        for i in range(n):
            if customers[i] == 'N':
                npen[i + 1] = npen[i] + 1
            else:
                npen[i + 1] = npen[i]

        for i in range(n-1,-1,-1):
            if customers[i] == 'Y':
                ypen[i] = ypen[i + 1] + 1
            else:
                ypen[i] = ypen[i + 1]

        minhr = 0
        minpen = 10**18

        for j in range(n+1):
            pen = npen[j] + ypen[j]
            if pen < minpen:
                minpen = pen
                minhr = j

        return minhr

        
        
        

