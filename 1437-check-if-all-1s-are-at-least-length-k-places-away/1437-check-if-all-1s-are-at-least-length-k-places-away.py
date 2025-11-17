class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        t=0
        f=False
        for i in nums:
            if i==0:
                t+=1
            else:
                if t<k and f:
                    return False
                t=0
                f=True
        return True

