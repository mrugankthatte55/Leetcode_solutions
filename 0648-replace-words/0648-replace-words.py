class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # dictionary.sort()
        # s=list(sentence.split(" "))
        # for i in range(len(s)):
        #     # f=0
        #     for j in dictionary:
        #         # if s[i][:len(j)] == j and f == 0:
        #         if s[i][:len(j)] == j:
        #             s[i]=j
        #             # f=1
        # listToStr = ' '.join([str(c) for c in s])
        # return listToStr
        
        d={}
        for i in dictionary:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=list(sentence.split(" "))
        for j in d:
            for i in range(len(s)):
                if s[i][:len(j)] == j:
                    s[i]=j
        listToStr = ' '.join([str(c) for c in s])
        return listToStr
        
# Gives TLE
# regex=re.compile('^hello')
# if re.match(regex, somestring):
#     print("Yes")


# can also use string.startswith()

