class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==1:
            return True
        if c==2:
            return True
        if c==0:
            return True
        # for i in range((c//2) +1):
        #     if c-(i**2)>0:
        #         x=math.sqrt(c-(i**2))
        #         if x==int(x):
        #             return True
        # return False
        d=set()
        for i in range(int(math.sqrt(c))+1):
            # d[i**2]=1
            d.add(i**2)
        # print(d)
        # 0 1 2 3
        for i in d:
            if c-i in d:
                return True
        return False