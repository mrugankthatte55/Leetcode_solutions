class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # mid=len(letters)//2
        # l=0
        # r=len(letters)-1
        # while l<=r:
        #     mid=(l+r)//2
        #     if letters[mid]>target:
        #         r=mid-1
        #     else:
        #         l=mid+1
        # return letters[l%len(letters)]
        
        # for c in letters:
        #     if c>target:
        #         return c
        # return letters[0]
        l=set(letters)
        target=ord(target)
        # c=Counter(letters)
        ans=ord(letters[0])
        for i in range(target+1,ord('z')+1):
            if chr(i) in l:
                return chr(i)
        return chr(ans)
