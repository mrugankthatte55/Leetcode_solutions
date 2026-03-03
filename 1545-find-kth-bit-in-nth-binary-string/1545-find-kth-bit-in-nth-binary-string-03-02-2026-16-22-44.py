class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(sn):
            return ''.join('1' if x == '0' else '0' for x in sn)

            # for i in range(len(sn)):
            #     if sn[i]=="1":
            #         sn[i]="0"
            #     else:
            #         sn[i]="1"
        sn="0"
        if n==1:
            return sn
        for i in range(2,n+1):
            sn=sn+"1"+invert(sn)[::-1]
        return sn[k-1]