# class Solution:
#     def longestBalanced(self, s: str) -> int:
#         def isbalanced(s):
#             d={}
#             for i in s:
#                 if i in d:
#                     d[i]+=1
#                 else:
#                     d[i]=1
#             return len(set(d.values()))==1
#             # s.sort()
#             # i=0
#             # while i<len(s):
#             #     if s[i]==s[0]:
#             #         i+=1
            
#         if isbalanced(s):
#             return len(s)
#         n=len(s)
#         currlen=n
#         while currlen>0:
#             for i in range(n-currlen):
#                 print(s[i:currlen+i])
#                 if isbalanced(s[i:currlen+i]):
#                     return currlen
#             currlen-=1
#         return 1
#         # for i in range(len(s)-1):
#         #     for j in range(i+1,len(s)):
#         #         if len(s[i:j+1])>ans and isbalanced(s[i:j+1]):
#         #             ans=len(s[i:j+1])
#                 # if isbalanced(s[i:j+1]):
#                 #     ans=max(ans,len(s[i:j+1]))
#         return ans
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                if len(set(cnt.values())) == 1:
                    res = max(res, j - i + 1)
        return res