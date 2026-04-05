class Solution:
    def judgeCircle(self, moves: str) -> bool:
        p=[0,0]
        for s in moves:
            if s=="U":
                p[0]+=1
            if s=="D":
                p[0]-=1
            if s=="L":
                p[1]-=1
            if s=="R":
                p[1]+=1
        if p==[0,0]:
            return True
        return False