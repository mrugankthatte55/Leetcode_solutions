class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        count = 0
        while xor_result:
            xor_result &= xor_result - 1
            count += 1
        return count
# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:
#         def getBinaryList(x):
#             res = []
#             bit = 1
#             while x > 0:
#                 if x & 1:
#                     res.append(1)
#                 else:
#                     res.append(0)
#                 x = x >> 1
#                 bit = bit << 1
#             # res.reverse()
#             return res
#         start=getBinaryList(start)
#         goal=getBinaryList(goal)
#         if len(start)>len(goal):
#             for i in range(len(start)-len(goal)):
#                 goal.append(0)
#         elif len(start)<len(goal):
#             for i in range(len(goal)-len(start)):
#                 start.append(0)
#         start.reverse()
#         goal.reverse()
#         ans=0
#         for i in range(len(start)):
#             if goal[i]!=start[i]:
#                 ans+=1
#         return ans