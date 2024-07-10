class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=0
        for i in logs:
            if i=="./":
                continue
            if i=="../" and st!=0:
                st-=1
            elif i!="../":
                st+=1
            print(st)
        return st