class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        l=[0]*len(customers)
        r=[0]*len(customers)
        if grumpy[0]==0:
            l[0]=customers[0]
        else:
            l[0]=0
        for i in range(1,len(customers)):
            if not grumpy[i]:
                l[i]=l[i-1]+customers[i]
            else:
                l[i]=l[i-1]
        # print(l)
        
        if not grumpy[-1]:
            r[-1]=customers[-1]
        else:
            r[-1]=0
        for i in range(len(customers)-2,-1,-1):
            if not grumpy[i]:
                r[i]=r[i+1]+customers[i]
            else:
                r[i]=r[i+1]
        # print(r)
        left=0
        right=minutes-1
        ans=0
        while left<=len(grumpy)-minutes and right<len(grumpy):
            s=0
            for i in range(left,right+1):
                s+=customers[i]
                # print(customers[i])
            # print("-------")
            if left>0:
                s+=l[left-1]
            if right<len(grumpy)-1:
                s+=r[right+1]
            if s>ans:
                ans=s
            left+=1
            right+=1
            
        return ans
        