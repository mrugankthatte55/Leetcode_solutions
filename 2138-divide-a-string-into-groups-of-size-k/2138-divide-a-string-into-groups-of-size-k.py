class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans=[]
        # if len(s)<
        if len(s)%k!=0:
            for i in range(k-(len(s)%k)):
                s+=(fill)
        for i in range(0,len(s),k):
            ans.append(s[i:i+k])
            
        return ans


        # ans=[]
        # kdash=1
        # sdash=''
        # for i in s:
        #     if k>kdash:
        #         sdash+=i
        #     if k==kdash:
        #         sdash+=i
        #         ans.append(sdash)
        #     if k<kdash:
        #         sdash=i
        #         kdash=1
        #     kdash+=1
        # print(sdash)
        # if len(sdash)<k:
        #     for i in range(k-len(sdash)):
        #         sdash+=fill
        # ans.append(sdash)
        # return ans

