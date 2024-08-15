



class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash={5:0, 10:0, 20:0}
        for i in bills:
            if i==5:
                cash[5]+=1
            elif i==10:
                if cash[5]==0:
                    return False
                cash[10]+=1
                cash[5]-=1
            else:
                if cash[10] > 0 and cash[5] > 0:
                    cash[5] -= 1
                    cash[10] -= 1
                elif cash[5] >= 3:
                    cash[5] -= 3
                else:
                    return False
        return True
    
        