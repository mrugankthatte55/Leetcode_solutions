class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans=[words[0]]
        prev=groups[0]
        for i in range(1,len(groups)):
            if prev!=groups[i]:
                ans.append(words[i])
                prev=groups[i]
        return ans