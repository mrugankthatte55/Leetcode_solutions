class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if (i!=j) and (words[i] in words[j]) and (words[i] not in ans):
                    ans.append(words[i])

        return ans
