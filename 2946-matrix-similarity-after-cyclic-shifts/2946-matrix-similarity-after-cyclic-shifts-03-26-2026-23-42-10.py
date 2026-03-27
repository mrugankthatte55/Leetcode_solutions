class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        mat2 = copy.deepcopy(mat)
        for i in range(k):
            for j in range(len(mat2)):
                if j%2==0:
                    mat2[j].append(mat2[j].pop(0))

                else:
                    mat2[j].insert(0,mat2[j].pop())
        #     print(mat2)
        # print(mat)
        # print(mat2)
        if mat2==mat:
            return True
        return False