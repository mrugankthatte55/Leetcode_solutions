class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        s=list(sentence.split(" "))
        for i in range(len(s)):
            f=0
            for j in dictionary:
                if s[i].startswith(j) and f==0:
                    s[i]=j
                    f=1
        listToStr = ' '.join([str(c) for c in s])
        return listToStr