# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
#         candidates.sort()
#         if candidates[0]>target:
#             return []
#         for i in range(len(candidates)-1,-1):
#             if candidates[i]>target:
#                 candidates.pop()
#             else:
#                 break
#         if sum(candidates)==target:
#             return [candidates]
        
        
#         def backtrack(start, path, target):
#             if target == 0:
#                 ans.append(path)
#                 return
#             if target < 0:
#                 return

#             for i in range(start, len(candidates)):
#                 if i > start and candidates[i] == candidates[i - 1]:
#                     continue
#                 backtrack(i + 1, path + [candidates[i]], target - candidates[i])

#         ans = []
#         backtrack(0, [], target)
#         return ans


        
        
        
# #         if sum(candidates)<target:
# #             return []
        
#         # ans=set([])
        
# #         n = int(math.pow(2, len(candidates)))

# #         for i in range( 1, n) :
# #             temp=[]
# #             for j in range(0, n) :
                
# #                 if (i & (1<<j)) :
# #                     temp.append(candidates[j])

# #             if sum(temp)==target:
# #                 temp.sort()
# #                 ans.add(tuple(temp))
# #         return ans

class Solution:
    def combinationSum2(self, candidates, target):
        answer = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], answer)
        return answer

    def backtrack(self, candidates, target, totalIdx, path, answer):
        if target < 0:
            return  # backtracking
        if target == 0:
            answer.append(path)
            return  # end
        for i in range(totalIdx, len(candidates)):
            if i > totalIdx and candidates[i] == candidates[i - 1]:
                continue
            self.backtrack(
                candidates,
                target - candidates[i],
                i + 1,
                path + [candidates[i]],
                answer,
            )