class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # ans=0
        # d={}
        # for i in range(len(s)):
        #     if s[i] in d:
        #         d[s[i]]+=1
        #     else:
        #         d[s[i]]=1
        # for i in d:
        #     ans+=(((d[i]*d[i]) + d[i])//2)
        # return ans
        n = len(s)
        answer = 0
        prefix_count = [0] * 26

        for i in range(len(s)):
            # Increment the number of times we encountered the current letter so far.
            prefix_count[ord(s[i]) - ord("a")] += 1

            # Current letter can be paired with all the occurrences of it that
            # comes before, including itself, to form a valid substring.
            answer += prefix_count[ord(s[i]) - ord("a")]

        return answer
    