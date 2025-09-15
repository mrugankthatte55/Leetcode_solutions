class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        spaces=0
        broken=0
        fl=0
        for ch in text:
            
            if ch in brokenLetters and fl==0:
                broken+=1
                fl=1

            if ch==" ":
                spaces+=1
                fl=0
        return spaces+1-broken
